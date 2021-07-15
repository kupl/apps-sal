import collections
import sys

input = sys.stdin.readline

class common_function():
    """
        1. よく使いそうで予め用意してあるものをまとめた
        2. よく使いそうな関数群をまとめた
    """
    def nCk(self, n:int, k:int):
        """
            mod を使用しない combination nCk を求めるメソッド
            1回 の nCk を求めるのに O(k) かかる.
        """
        k = min(k, n-k)
        numer = 1
        for i in range(n, n-k, -1):
            numer *= i
        denom = 1
        for i in range(k, 1, -1):
            denom *= i
        return numer // denom

def main():
    common = common_function()
    N = int(input())
    slist = []
    tlist = []
    for _ in range(N):
        s = list(input()[:-1])
        s.sort()
        slist.append(s)
    slist.sort()
    cnt = 1; tlist.append(cnt)
    for i in range(N-1):
        if slist[i] == slist[i+1]:
            tlist.append(cnt)
        else:
            cnt += 1
            tlist.append(cnt)
    tlistcount = list(collections.Counter(tlist).items())
    tlistcount.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    for t0, t1 in tlistcount:
        if t1 == 1:
            break
        ans += common.nCk(t1, 2)
    print(ans)

def __starting_point():
    main()

__starting_point()

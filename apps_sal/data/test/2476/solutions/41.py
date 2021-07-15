import sys
from collections import Counter

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def main():
    n = int(input())
    aa = list(map(int, input().split()))
    aa = list(Counter(aa).values())
    aa.sort()
    cs = [0]
    s = 0
    for a in aa:
        s += a
        cs += [s]
    # print(aa)
    # print(cs)
    ans = n + 1
    i = len(aa)
    for k in range(1, n + 1):
        while 1:
            while i > 0 and aa[i - 1] >= ans:
                i -= 1
            s = cs[i] + ans * (len(aa) - i)
            if s >= ans * k:
                break
            else:
                ans -= 1
        print(ans)

main()


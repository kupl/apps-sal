# 参考 https://atcoder.jp/contests/abc140/submissions/7411285
import sys
input = sys.stdin.readline

def main():
    n = int(input()[:-1])
    aa = list(map(int, input().split()))
    ans = 0
    pos = [0] * (n + 1)
    for i, a in enumerate(aa):
        pos[a] = i + 2
    Lnext = [1, 1] + list(range(1, n + 1)) + [n, n]
    Rnext = [3, 3] + list(range(3, n + 3)) + [n + 2, n + 2]
    for a in range(1,n + 1):
        i = pos[a]
        l0 = Lnext[i]
        l1 = Lnext[l0]
        r0 = Rnext[i]
        r1 = Rnext[r0]
        ans += a * ((l0 - l1) * (r0 - i) + (i - l0) * (r1 - r0))
        Lnext[r0] = l0
        Rnext[l0] = r0
    print(ans)

main()


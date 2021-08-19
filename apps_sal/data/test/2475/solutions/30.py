import sys
input = sys.stdin.readline
N = int(input())
S = list(map(int, input().split()))
N -= 1
ans = 0
for d in range(1, N + 1):
    a = N - d
    res = 0
    (p, q) = (N, 0)
    while a >= d:
        if a <= N - a and N % d == 0:
            break
        p -= d
        q += d
        res += S[p] + S[q]
        if res > ans:
            ans = res
        a -= d
print(ans)

N, K = map(int, input().split())
S = input()

now = S[0]
a = -1
for s in S:
    a += now == s
    now = s
a += K * 2
ans = min(N - 1, a)
print(ans)

N, K = map(int, input().split())
A = list(map(int, input().split()))
RA = sorted(A)
RA = RA[::-1]
s = 0
ans = 0
for i in range(N):
    a = RA[i]
    if s + a < K:
        s += a
        ans += 1
    else:
        ans = 0
print(ans)

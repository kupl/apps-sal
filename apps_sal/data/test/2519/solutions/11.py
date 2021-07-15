N, K = list(map(int, input().split()))
p = list(map(int, input().split()))

I = [0] * N
for i in range(N):
    I[i] = (p[i] + 1) / 2

S = sum(I[:K])
ans = S
l = 0
r = K
while r < N:
    S = S - I[l] + I[r]
    ans = max(ans, S)
    l += 1
    r += 1

print(ans)
return




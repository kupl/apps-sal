N,K = list(map(int,input().split()))
S = []
d = {}
A = list(map(int,input().split()))
ans = 0
sum =0
for i in range(1,N+1):
    sum += A[i-1] % K
    s = (sum - i) % K
    if i > K:
        x = S.pop(0)
        d[x] -= 1
    elif i < K:
        if s == 0:
            ans += 1
    if s not in d:
        d[s] = 0
    ans += d[s]
    d[s] += 1
    S.append(s)
print(ans)


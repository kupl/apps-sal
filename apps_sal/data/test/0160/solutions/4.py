def divisor(n):
    res = []
    i = 1
    while i*i <= n:
        if n%i == 0:
            res.append(i)
            if i*i != n:
                res.append(n//i)
        i += 1
    res.sort()
    return res

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
S = sum(A)
ans = 1
for d in divisor(S):
    rs = [a%d for a in A]
    rs.sort()
    Sum = [0]*(N+1)
    Sum2 = [0]*(N+1)
    for i in range(1,N+1):
        Sum[i] = Sum[i-1]+rs[i-1]
        Sum2[i] = Sum2[i-1]+(d-rs[i-1])
    for i in range(N+1):
        if Sum[i] == Sum2[N]-Sum2[i]:
            if Sum[i] <= K:
                ans = d
print(ans)


N = int(input())
A = list(map(int,input().split()))
ABI = sorted(((a, i) for i, a in enumerate(A, 1)), reverse=True)
prev = [0]
for k, (a, i) in enumerate(ABI):
    curr = [0]*(k+2)
    for l in range(k+1):
        curr[l] = max(curr[l], prev[l] + a*abs(N-i-(k-l)))
        curr[l+1] = prev[l]+a*abs(i-l-1)
    prev = curr
print (max(prev))

N, K = map(int, input().split())
d = [0]*K
A = [0 for _ in range(K)]
for i in range(K):
    d[i] = int(input())
    A[i] = list(map(lambda x: int(x)-1, input().split()))


#print(A)
sunukes = [0]*N
for i in range(K):
    for j in range(d[i]):
        #print(A[i][j])
        sunukes[A[i][j]] += 1
#print(sunukes)
ans = 0
for s in range(N):
    if sunukes[s] == 0:
        ans += 1

print(ans)

N, K = map(int, input().split())
P = list(map(int, input().split()))
P = [sum(P[:K])+K]+P
for i in range(N-K):
    P[i+1] = P[i]-P[i+1]+P[K+i+1]
print(max(P[:N-K+1])/2)

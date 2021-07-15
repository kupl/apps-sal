N,M = map(int,input().split())
lsA = list(map(int,input().split()))
sumA = sum(lsA)
print(max(-1,N-sumA))

n = int(input())
L = list(map(int,input().split()))
L.sort()
print(L[n-1]-L[0])

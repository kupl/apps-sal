a,b,n = map(int,input().split())

k = max(0,(n - b + 1) // b)
k = min(n,k * b + b - 1)

print((a * k) // b - a * (k // b))

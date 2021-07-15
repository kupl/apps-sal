n,k = list(map(int, input().split()))

mw = n//2

d = mw//(k+1)

print(d, k*d, n-d*(1+k))



n,x,pos = list(map(int,input().split()))

a = [i for i in range(n)]

zero = 0
one = 0

left = 0
right = n
while left<right:
    middle = (left + right)//2
    if a[middle]<=pos:
        zero += 1
        left = middle+1
    else:
        one += 1
        right = middle

res = 1
mod = 10**9+7
for i in range(zero-1):
    res *= (x-1-i)
    res %= mod
for i in range(one):
    res *= (n-x-i)
    res %= mod

for j in range(n-zero-one):
    res *= j+1
    res %= mod

print(res)


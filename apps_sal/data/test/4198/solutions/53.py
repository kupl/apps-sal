a, b, x = list(map(int, input().split()))

l, r = 0, 10**9+1
while l+1 < r:
    n = (l+r)//2
    if a*n + b*len(str(n)) > x:
        r = n
    else:
        l = n
print(l)


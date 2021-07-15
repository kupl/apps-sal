n, k, m = list(map(int, input().split()))
t = sorted(map(int, input().split()))
st = sum(t)
res = 0
for x in range(min(m//st,n)+1):
    rem = m - x*st
    r = x*(k+1)
    for i in range(k):
        div = min(rem//t[i], n-x) 
        rem -= div*t[i]
        r += div
    res = max(res, r)
print(res)

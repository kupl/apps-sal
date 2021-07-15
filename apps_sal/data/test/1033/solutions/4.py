n , h = list(map(int , input().split()))
l = 1;r = 10 ** 10
while(r - l > 1):
    mid = ((l + r) >> 1)
    if(mid <= h):
        calc = (mid + 1) * mid
        calc = (calc >> 1)
        if(calc > n):
            r = mid
        else:
            l = mid
        continue
    calc = (mid + 1) * mid
    calc = (calc >> 1)
    calc += ((mid + h - 1) * (mid - h )) // 2
    if(calc > n):
        r = mid
    else:
        l = mid
ans = l
if(l > h):
    ans += l - h 
calc = (l + 1) * l;calc = (calc >> 1)
if(l > h):calc += ((l + h - 1) * (l - h)) // 2
n -= calc
ans += n // l
n %= l
if(n > 0):
    ans += 1
print(ans)


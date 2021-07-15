a, b = list(map(int, input().split(' ')))
x = list(map(int, input().split(' ')))

def f(num):
    lo = 0
    hi = a-1
    ct = 0
    while lo <= hi:
        if lo == hi:
            ct += 1
            break
        if x[lo] + x[hi] <= num:
            lo+=1
            hi-=1
        else:
            hi-=1
        ct+=1
    return ct

lo = max(x)
hi = 100000000
while lo < hi:
    mid = (lo + hi) // 2
    if f(mid) > b:
        lo = mid + 1
    else:
        hi = mid

print(lo)


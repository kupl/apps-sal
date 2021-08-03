a, b, x = map(int, input().split())
mx = 10**9 + 1
mn = 0

while(mx - mn > 1):
    mid = (mx + mn) // 2
    p = a * mid + b * len(str(mid))
    if(p <= x):
        mn = mid
    else:
        mx = mid

print(mn)

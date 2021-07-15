a,ta = list(map(int,input().split()))
b,tb = list(map(int,input().split()))
h,m = list(map(int,input().split(":")))
m += h * 60
mint = m - tb
maxt = m + ta
m2 = 300
ans = 0
while 1440 > m2:
    if m2 > mint and maxt > m2:
        ans += 1
    m2 += b
print(ans)


def inum2(num):
    if num > int(num):
        return int(num) + 1
    else:
        return int(num)
v1, v2 = list(map(int,input().split()))
t, d = list(map(int,input().split()))
nowv = v1
s = 0
i = 1
if d > 0:
    while t + 1 > i: 
        s += nowv
        nowv = min(nowv + d,v2+(t-i-1)*d)
        i += 1
    print(s)
else:
    print(v1 * t)


n, k = map(int,input().split())
s = list(input())

cl = 0
cr = 0
a = []
ans = 0
if s[0] == '1':
    ck = 0
    ans = 1
else:
    ck = 1
    a.append([0,0])
while True:
    while ck <= k and cr < n-1:
        cr += 1
        if s[cr-1] == '1' and s[cr] == '0':
            if ck < k:
                ck += 1
                a.append([cr, cr])
            else:
                break
        elif s[cr-1] == '0' and s[cr] == '1':
            a[-1][1] = cr
        ans = max(ans, cr - cl + 1)
    if cr < n-1:
        tl, tr = a.pop(0)
        cl = tr
        cr -= 1
        ck -= 1
    else:
        break
print(ans)

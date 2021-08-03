h, m, s, t1, t2 = list(map(int, input().split()))

if(h == 12):
    h = 0
h = h * 60 * 60 + m * 60 + s
m = m * 12 * 60 + s

s = s * 12 * 60

if(t1 == 12):
    t1 = 0
if(t2 == 12):
    t2 = 0

t1 = t1 * 60 * 60
t2 = t2 * 60 * 60

# print(h,m,s,t1,t2)

i = t2
once = True
while(True):
    if i == h or i == m or i == s:
        break
    i += 1
    if i == 12 * 60 * 60:
        if once:
            i = 0
            once = False
        else:
            break
    if i == t1:
        print("YES")
        return
i = t1
once = True
while(True):
    if i == h or i == m or i == s:
        break
    i += 1
    if i == 12 * 60 * 60:
        if once:
            i = 0
            once = False
        else:
            break
    if i == t2:
        print("YES")
        return

print("NO")

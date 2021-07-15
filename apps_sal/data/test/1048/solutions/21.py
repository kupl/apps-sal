t = int(input())
a = input()
l,r,d,u = 0,0,0,0
for i in a:
    if i == 'L': l+=1
    if i == 'R': r+=1
    if i == 'U': u+=1
    if i == 'D': d+=1
s = min(l,r)*2 + min(u,d)*2
print(s)

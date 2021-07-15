s = input().split()
l, r, a = int(s[0]), int(s[1]), int(s[2])
x = min(l, r)
y = max(l, r)
while(a!=0 and x!=y):
    x+=1
    a-=1

print(min(x, y)*2 + a//2*2)

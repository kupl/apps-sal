n = int(input())
s = input()
t = 0
mn = 0
for i in s:
    if i == '-':
        t-=1
    else:
        t+=1
    mn = min(mn, t)
print(-mn+t)

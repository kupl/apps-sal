s = list(input())
t = list(input())
l = min(len(s),len(t))
if len(s)>len(t):
    x = 1
elif len(s)<len(t):
    x = 2
else:
    x = 0
for i in range(l):
    print(s[i],end = "")
    print(t[i],end = "")
if x == 1:
    print(s[-1])
elif x == 2:
    print(t[-1])

n = int(input())
s = list(map(int,input().split()))
a,b = -1,188888
for t in range(1,101):
    mi = 0
    for i in range(n):
        mi += min(abs(s[i]-t),abs(s[i]-t-1),abs(s[i]-t+1))
    if b>mi:
        a,b = t,mi
print(a,b)

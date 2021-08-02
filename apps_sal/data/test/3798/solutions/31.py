n = int(input())
s = int(input())
if(n < s):
    print(-1)
    return
elif(n == s):
    print(n + 1)
    return

lim = 10**6
for i in range(2, lim + 1):
    tmp = 0
    x = n
    while(x > 0):
        tmp += x % i
        x //= i
    if(tmp == s):
        print(i)
        return

# 2桁
ns = n - s
inf = 10**12
ans = inf
for i in range(1, ns + 1):
    if(i**2 > ns):
        break

    if(ns % i == 0):
        b = ns // i + 1
        y = n - (b * i)
        if(i + y == s) & (0 <= y < b):
            ans = min(ans, b)

if(ans == inf):
    print(-1)
else:
    print(ans)

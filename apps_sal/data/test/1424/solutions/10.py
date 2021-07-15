n,m,r = map(int,input().split())
a = []
for i in range(m+1):
    s = bin(int(input()))[2:]
    t = str()
    for i in range(21 - len(s) + 1):
        t += '0'
    a.append(t + s)

res = 0
t = a[len(a)-1]
for i in range(len(a)-1):
    ans = 0
    for k in range(len(t)):
        if t[k] != a[i][k]:
            ans += 1
    if ans <= r:
        res += 1
print(res)

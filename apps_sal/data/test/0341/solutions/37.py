n,k = (int(x) for x in input().split())
r,s,p = (int(x) for x in input().split())
t = input()
a = []
ans = 0

for i in range(0,n):
    a.append(t[i])

for j in range(0,n):
    if j - k >= 0 and a[j - k] == a[j]:
           a[j] = "o"
    p
    if a[j] == "r":
        ans = ans + p
    if a[j] == "s":
        ans = ans + r
    if a[j] == "p":
        ans = ans + s


print(ans)

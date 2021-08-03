def intin(): return list(map(int, input().split()))
def Ain(): return list(map(int, input().split()))


mod = 1000000007

n, k = intin()
a = Ain()
m = n + 1

f = [-1] * m
l = [-1] * m

for i in range(k):
    x = a[i]
    if f[x] == -1:
        f[x] = i
    l[x] = i

ans = 0
for i in range(1, m):
    if f[i] == -1:
        ans += 1
        if i > 1:
            ans += 1
        if i < n:
            ans += 1
        continue
    if i < n and f[i] > l[i + 1]:
        ans += 1
    if i > 1 and f[i] > l[i - 1]:
        ans += 1
print(ans)

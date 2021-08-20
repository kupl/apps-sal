(n, k, x) = list(map(int, input().split()))
a = list(map(int, input().split()))
c = x ** k
pr = [0]
su = [0]
b = 0
for i in range(n - 1):
    b = a[i] | b
    pr.append(b)
b = 0
for i in range(n - 1, 0, -1):
    b = a[i] | b
    su.append(b)
su = su[::-1]
d = []
for i in range(n):
    d.append(pr[i] | a[i] * c | su[i])
print(max(d))

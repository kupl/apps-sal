t = input().split()
n = int(t[0])
r = int(t[1])
avg = int(t[2])
a = []
for i in range(n):
    a.append(input().split())
    t = int(a[i][0])
    a[i][0] = int(a[i][1])
    a[i][1] = t
a = sorted(a)
ref = 0
new = 0
for i in range(n):
    new += a[i][1]
new /= n
i = 0
while new < avg and i < n:
    x = min(r - a[i][1], round((avg - new) * n))
    new += 1 / n * x
    ref += a[i][0] * x
    i += 1
print(round(ref))

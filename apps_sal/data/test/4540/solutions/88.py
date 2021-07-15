n = int(input())
a = list(map(int, input().split()))

d = [abs(a[0])]
for i in range(n-1):
    d.append(abs(a[i+1] - a[i]))

d.append(abs(a[-1]))

s = sum(d)

for i in range(n):
    if i == 0:
        t = s - d[i] - d[i+1] + abs(a[i+1])
    elif i == n-1:
        t = s - d[i] - d[i+1] + abs(-a[i-1])
    else:
        t = s - d[i] - d[i+1] + abs(a[i+1] - a[i-1])
    print(t)

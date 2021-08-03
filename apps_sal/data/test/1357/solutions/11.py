n, m = map(int, input().split())
a = [1] + list(map(int, input().split()))
a1 = []
t = 0
for i in a:
    a1.append(i - 1)
for i in range(0, len(a1) - 1, 1):
    if(a[i + 1] >= a[i]):
        t += a[i + 1] - a[i]
    else:
        t += n - a[i] + a[i + 1]

print(t)

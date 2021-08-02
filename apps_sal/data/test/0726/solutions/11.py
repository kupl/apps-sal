n, d = input().split()
n = int(n)
d = int(d)
a = list(map(int, input().split()))
t = 2
for i in range(n - 1):
    if a[i + 1] - a[i] > 2 * d:
        t += 2
    elif a[i + 1] - a[i] == 2 * d:
        t += 1
print(t)

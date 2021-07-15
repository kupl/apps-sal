n, x = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))
s = 0
for i in range(n):
    s += a[i] * max(1, x - i)
print(s)


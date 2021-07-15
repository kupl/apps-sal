n = int(input())
a = []
s = 0
for _ in range(n):
    t = list(map(int, input().split()))
    s += t[1] * n - t[0]
    a.append(t[0] - t[1])
a.sort()
for i in range(n):
    s += a[i] * (n - i)
print(s)


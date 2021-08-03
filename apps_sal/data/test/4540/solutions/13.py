n = int(input())
a = list(map(int, input().split()))
a.insert(n, 0)
a.insert(0, 0)
t = 0
tmp = 0
for i in range(n + 1):
    t += abs(a[i + 1] - a[i])
for i in range(1, n + 1):
    tmp = t
    tmp -= abs(a[i] - a[i - 1]) + abs(a[i + 1] - a[i])
    tmp += abs(a[i + 1] - a[i - 1])
    print(tmp)

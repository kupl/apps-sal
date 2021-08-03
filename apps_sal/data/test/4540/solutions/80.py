n = int(input())
a = [int(t) for t in input().split()]
a.insert(0, 0)
a.append(0)
s = 0
for i in range(1, n + 2):
    s += abs(a[i - 1] - a[i])
for i in range(1, n + 1):
    if a[i - 1] <= a[i] <= a[i + 1] or a[i - 1] >= a[i] >= a[i + 1]:
        print(s)
    else:
        res = s
        res -= abs(a[i - 1] - a[i])
        res -= abs(a[i] - a[i + 1])
        res += abs(a[i - 1] - a[i + 1])
        print(res)

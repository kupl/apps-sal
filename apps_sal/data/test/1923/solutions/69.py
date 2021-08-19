n = int(input())
a = list(map(int, input().split()))
a.sort()
c = 0
for i in range(0, n):
    c += min(a[2 * i], a[2 * i + 1])
print(c)

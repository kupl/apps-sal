n = int(input())
a = list(map(int, input().split()))
print(2 * n - 2)
M = a.index(max(a))
m = a.index(min(a))
if abs(a[m]) <= abs(a[M]):
    for i in range(n):
        if i != M:
            print((M + 1, i + 1))
    for i in range(n - 1):
        print((i + 1, i + 2))
else:
    for i in range(n):
        if i != m:
            print((m + 1, i + 1))
    for i in range(1, n)[::-1]:
        print((i + 1, i))

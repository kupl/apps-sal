n = int(input())
a, b = [], []
for i in range(n):
    c, d = map(int, input().split())
    a.append(c)
    b.append(d)
a.sort()
b.sort(reverse=True)
if n % 2 == 1:
    ac = a[(n + 1) // 2 - 1]
    bc = b[(n + 1) // 2 - 1]
    ans = bc - ac
else:
    ac = (a[n // 2 - 1] + a[n // 2])
    bc = (b[n // 2 - 1] + b[n // 2])
    ans = bc - ac
print(ans + 1)

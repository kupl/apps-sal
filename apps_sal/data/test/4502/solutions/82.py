n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    b.append(0)
k = 0
if n % 2 == 1:
    k = (n - 1) // 2
    m = -1
else:
    k = n // 2
    m = 1
for i in range(n):
    if i % 2 == 0:
        b[k + m * i // 2] = a[i]
    else:
        b[k - m * (i + 1) // 2] = a[i]
ans = ''
for i in range(n):
    ans += str(b[i]) + ' '
print(ans)

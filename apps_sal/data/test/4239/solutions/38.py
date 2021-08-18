
n = int(input())

ans = n

for i in range(n + 1):
    c = 0
    a = n - i
    while a > 0:
        c += a % 6
        a = a // 6
    a = i
    while a > 0:
        c += a % 9
        a = a // 9
    if c < ans:
        ans = c

print(ans)

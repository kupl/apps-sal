(n, m) = map(int, input().split())
ans2 = 0
if (n + 1) // 2 > m:
    print(n - m * 2, end=' ')
else:
    print(0, end=' ')
for i in range(n, -1, -1):
    now = n - i
    if now * (now - 1) // 2 >= m:
        print(i)
        break

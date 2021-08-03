n, a, b = map(int, input().split())

ans = 0
for i in range(1, n + 1):
    w = sum(list(map(int, list(str(i)))))
    if a <= w and w <= b:
        ans += i
print(ans)

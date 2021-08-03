n, a, b = map(int, input().split())
ans = 0
for i in range(1, n + 1):
    l = len(str(i))
    total = 0
    for j in range(1, l + 1):
        total += int(str(i)[-j])
    if a <= total and total <= b:
        ans += i
print(ans)

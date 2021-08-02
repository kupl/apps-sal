n = int(input())
ans = 0
for i in range(1, n + 1):
    if n >= 2 * i:
        ans += i
    else:
        ans += n - i + 1
print(ans)

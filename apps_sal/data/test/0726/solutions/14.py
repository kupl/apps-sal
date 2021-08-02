n, d = list(map(int, input().split()))
x = list(map(int, input().split()))

ans = 2
for i in range(n - 1):
    if x[i + 1] - x[i] == 2 * d:
        ans += 1
    elif x[i + 1] - x[i] > 2 * d:
        ans += 2
print(ans)

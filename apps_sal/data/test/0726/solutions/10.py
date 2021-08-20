(n, d) = list(map(int, input().split()))
data = list(map(int, input().split()))
ans = 1
for i in range(n):
    if i == 0:
        ans += 1
        continue
    if data[i] - data[i - 1] >= 2 * d:
        if data[i] - data[i - 1] != 2 * d:
            ans += 2
        else:
            ans += 1
print(ans)

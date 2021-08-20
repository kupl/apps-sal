(n, d) = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]
ans = 2
for i in range(1, len(x)):
    if x[i] - x[i - 1] == 2 * d:
        ans += 1
    if x[i] - x[i - 1] > 2 * d:
        ans += 2
print(ans)

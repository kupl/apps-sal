n, d = list(map(int, input().split()))
koord = list(map(int, input().split()))
ans = 2
sums = []
for i in range(1, n):
    sums.append(koord[i] - koord[i - 1])
for i in sums:
    if i > 2 * d:
        ans += 2
    elif i == 2 * d:
        ans += 1
print(ans)

(n, k) = list(map(int, input().split()))
d = list(map(int, input().split()))
ost = [0] * k
for i in range(n):
    ost[d[i] % k] += 1
ans = ost[0] // 2
for i in range(1, k // 2 + 1):
    if i != k - i:
        ans += min(ost[i], ost[k - i])
    else:
        ans += ost[i] // 2
print(ans * 2)

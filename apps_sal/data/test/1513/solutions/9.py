n, m, k = list(map(int, input().split()))
b = list(map(int, input().split()))
b_dif = []
for i in range(n - 1):
    b_dif.append(b[i + 1] - b[i])
b_dif.sort()
ans = k
for i in range(n - k):
    ans += b_dif[i]
print(ans)

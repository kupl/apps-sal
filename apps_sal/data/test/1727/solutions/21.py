n = int(input())
x = [0] * n
h = [0] * n
for i in range(n):
    (x[i], h[i]) = map(int, input().split())
ans = min(n, 2)
k = x[0]
for i in range(1, n - 1):
    if x[i] - h[i] > k:
        ans += 1
        k = x[i]
    elif x[i] + h[i] < x[i + 1]:
        ans += 1
        k = x[i] + h[i]
    else:
        k = x[i]
print(ans)

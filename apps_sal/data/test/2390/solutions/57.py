n, c = list(map(int, input().split()))

x = [0] * n
v = [0] * n
for i in range(n):
    x[i], v[i] = list(map(int, input().split()))

x = [0] + x + [c]
v = [0] + v + [0]

left = [0] * (n + 2)
right = [0] * (n + 2)

for i in range(n + 1):
    left[i + 1] = left[i] + v[i + 1] - (x[i + 1] - x[i])
for i in range(n + 1, 0, -1):
    right[i - 1] = right[i] + v[i - 1] - (x[i] - x[i - 1])


for i in range(n + 1):
    left[i + 1] = max(left[i + 1], left[i])
for i in range(n + 1, 0, -1):
    right[i - 1] = max(right[i - 1], right[i])

# 引き返さない最大
ans = max(left[-1], right[0])
right = list(reversed(right))
for i in range(n):
    tmp = left[i] - x[i]
    rem = n - i
    ans = max(ans, tmp + right[n - i])

for i in range(n):
    tmp = right[i] - (c - x[-(i + 1)])
    rem = n - i
    ans = max(ans, tmp + left[n - i])

print(ans)


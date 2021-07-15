N, C = map(int, input().split())

sushi = []
for i in range(N):
    x, v = map(int, input().split())
    sushi.append((x, v))

left = [0] * N
left2 = [0] * N
right = [0] * N
right2 = [0] * N

d = 0
d2 = 0
cal = 0
for i in range(N):
    x, v = sushi[i]
    d = x
    d2 = x * 2
    cal += v
    if i == 0:
        right[i] = max(cal - d, 0)
        right2[i] = max(cal - d2, 0)
    else:
        right[i] = max(cal - d, right[i-1])
        right2[i] = max(cal - d2, right2[i-1])

d = 0
d2 = 0
cal = 0
for i in reversed(range(N)):
    x, v = sushi[i]
    d = C - x
    d2 = (C - x) * 2
    cal += v
    if i == 0:
        left[i] = max(cal - d, 0)
        left2[i] = max(cal - d2, 0)
    else:
        left[i] = max(cal - d, left[i-1])
        left2[i] = max(cal - d2, left[i-1])

ans = 0
# 左側を全部試す
for i in range(N):
    if i == 0:
        ans = max(ans, left[i])
    else:
        ans = max(ans, left[i] + right2[i-1])
# 右側を全部試す
for i in range(N):
    if i == N - 1:
        ans = max(ans, right[i])
    else:
        ans = max(ans, right[i] + left2[i+1])

print(ans)

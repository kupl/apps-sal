x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
n = int(input())
s = input()
X, Y = 0, 0
for c in s:
    if c in 'UD':
        Y += 1 if c == 'U' else -1
    else:
        X += 1 if c == 'R' else -1

lo = 0
hi = 2 * 10**9 + 10
ans = -1
while lo <= hi:
    curr = -1
    mid = (lo + hi) // 2
    cx, cy = x1, y1
    for i in range(n):
        dx = abs(x2 - X * mid - cx)
        dy = abs(y2 - Y * mid - cy)
        if dx + dy <= mid * n + i:
            val = mid * n + i
            curr = val if curr == -1 or curr > val else curr
        if s[i] in 'UD':
            cy += 1 if s[i] == 'U' else -1
        else:
            cx += 1 if s[i] == 'R' else -1
    if curr != -1:
        ans = curr if ans == -1 or ans > curr else ans
        hi = mid - 1
    else:
        lo = mid + 1
print(ans)

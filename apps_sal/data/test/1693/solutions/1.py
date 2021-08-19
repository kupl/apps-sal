n = int(input())
sp = list(map(int, input().split()))
forw = [0 for i in range(n)]
backw = [0 for i in range(n)]
stack = [(0, -1, 0)]
for i in range(n):
    while sp[i] <= stack[-1][0]:
        stack.pop()
    stack.append((sp[i], i, (i - stack[-1][1]) * sp[i] + stack[-1][2]))
    forw[i] = stack[-1][2]
revsp = sp[::-1]
stack = [(0, -1, 0)]
for i in range(n):
    while revsp[i] <= stack[-1][0]:
        stack.pop()
    stack.append((revsp[i], i, (i - stack[-1][1]) * revsp[i] + stack[-1][2]))
    backw[i] = stack[-1][2]
backw = backw[::-1]
center = 0
ans_center = 0
for i in range(n):
    if ans_center < backw[i] + forw[i] - sp[i]:
        center = i
        ans_center = backw[i] + forw[i] - sp[i]
ans = [0 for i in range(n)]
ans[center] = sp[center]
cur = sp[center]
for i in range(center - 1, -1, -1):
    cur = min(cur, sp[i])
    ans[i] = cur
cur = sp[center]
for i in range(center + 1, n, 1):
    cur = min(cur, sp[i])
    ans[i] = cur
print(*ans)

n = int(input())
m = list(map(int, input().split()))
(left, right) = ([m[0]], [m[n - 1]])
stack = [(m[0], 1)]
for i in range(1, n):
    res = left[-1]
    num_tmp = 0
    while stack and stack[-1][0] > m[i]:
        res -= stack[-1][0] * stack[-1][1]
        num_tmp += stack[-1][1]
        stack.pop()
    res += m[i] * (num_tmp + 1)
    stack.append((m[i], num_tmp + 1))
    left.append(res)
stack = [(m[n - 1], 1)]
for i in range(n - 2, -1, -1):
    res = right[-1]
    num_tmp = 0
    while stack and stack[-1][0] > m[i]:
        res -= stack[-1][0] * stack[-1][1]
        num_tmp += stack[-1][1]
        stack.pop()
    res += m[i] * (num_tmp + 1)
    stack.append((m[i], num_tmp + 1))
    right.append(res)
(maxi, maxi_ind) = (0, -1)
for i in range(n):
    if left[i] + right[n - i - 1] - m[i] > maxi:
        maxi = left[i] + right[n - i - 1] - m[i]
        maxi_ind = i
i = maxi_ind
ans = [0 for _ in range(n)]
num = m[i]
ans[i] = m[i]
cur = m[i]
for j in range(i - 1, -1, -1):
    cur = min(m[j], cur)
    ans[j] = cur
    num += cur
cur = m[i]
for k in range(i + 1, n):
    cur = min(m[k], cur)
    ans[k] = cur
    num += cur
print(*ans)

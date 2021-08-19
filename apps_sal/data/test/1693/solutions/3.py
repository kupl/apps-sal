from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
q = deque([])
ans = [0] * n
tmp_ans = 0
for i in range(n):
    ind = i
    l_ind = i
    while True:
        if not q:
            q.append((a[i], l_ind))
            tmp_ans += a[i] * (l_ind + 1)
            break
        if q[-1][0] <= a[i]:
            tmp_ans += a[i] * (l_ind - q[-1][1])
            q.append((a[i], l_ind))
            break
        else:
            (height, l) = q.pop()
            if not q:
                tmp_ans -= height * (l + 1)
            else:
                tmp_ans -= height * (l - q[-1][1])
            ind = l
    ans[i] = tmp_ans
b = a[::-1]
q = deque([])
ans2 = [0] * n
tmp_ans = 0
for i in range(n):
    ind = i
    l_ind = i
    while True:
        if not q:
            q.append((b[i], l_ind))
            tmp_ans += b[i] * (l_ind + 1)
            break
        if q[-1][0] <= b[i]:
            tmp_ans += b[i] * (l_ind - q[-1][1])
            q.append((b[i], l_ind))
            break
        else:
            (height, l) = q.pop()
            if not q:
                tmp_ans -= height * (l + 1)
            else:
                tmp_ans -= height * (l - q[-1][1])
            ind = l
    ans2[i] = tmp_ans
max_ans = 0
ind = -1
for i in range(n):
    tmp = ans[i] + ans2[n - 1 - i] - a[i]
    if max_ans < tmp:
        max_ans = tmp
        ind = i
i = ind
ans = [0] * n
tmp = a[i]
l = i
r = i
max_height = a[i]
ans[i] = a[i]
for j in range(0, l)[::-1]:
    if a[j] >= max_height:
        tmp += max_height
    else:
        tmp += a[j]
        max_height = a[j]
    ans[j] = max_height
max_height = a[i]
for j in range(r + 1, n):
    if a[j] >= max_height:
        tmp += max_height
    else:
        tmp += a[j]
        max_height = a[j]
    ans[j] = max_height
print(*ans)

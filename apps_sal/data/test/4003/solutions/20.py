N = int(input())
a_list = list(map(int, input().split()))
from collections import deque
import bisect

deq = deque(a_list)
ans = ""
left = 0
right = 0
min_num = -1
cnt = 0
f = False
lr = False
while len(deq) >= 2:
    left = deq.popleft()
    right = deq.pop()
    # print(left, right)
    max_num = max(left, right)
    if max_num > min_num:

        if left == right:
            deq.appendleft(left)
            deq.append(right)
            lr = True
            break
        cnt += 1
        if right > left > min_num:
            ans += "L"
            deq.append(right)
            min_num = left
        elif left > right > min_num:
            ans += "R"
            deq.appendleft(left)
            min_num = right
        elif left > min_num:
            ans += "L"
            deq.append(right)
            min_num = left
        else:
            ans += "R"
            deq.appendleft(left)
            min_num = right
    else:
        f = True
        break
if lr:
    l = 0
    r = 0
    tmp = deq.copy()
    prv = -1
    for t in tmp:
        if t > prv:
            l += 1
        else:
            break
        prv = t
    tmp = list(reversed(tmp))
    prv = -1
    for t in tmp:
        if t > prv:
            r += 1
        else:
            break
        prv = t
    if l > r:
        print(cnt + l)
        print(ans + "L" * l)
    else:
        print(cnt + r)
        print(ans + "R" * r)
    return


if f:
    print(cnt)
    print(ans)
else:
    tmp = deq.pop()
    if tmp > min_num:
        cnt += 1
        print(cnt)
        print(ans + "R")
    else:
        print(cnt)
        print(ans)


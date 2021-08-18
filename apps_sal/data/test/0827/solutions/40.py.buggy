# template
from collections import deque
def inputlist(): return [int(j) for j in input().split()]


# template
N = int(input())
T = input()

if N == 1:
    if T == '1':
        print((2 * (10**10)))
    else:
        print((10**10))
    return

if N == 2:
    if T == '11':
        print((10**10))
        return
    if T == '10':
        print((10**10))
        return
    if T == '01':
        print((10**10 - 1))
        return
    print((0))
    return

que = deque()

for i in range(N):
    if (i + 1) % 3 == 0:
        que.append('0')
    else:
        que.append('1')


count = 0
ans = -1
while count < 3:
    flag = 0
    if count == 0:
        li = list(que)
        t = ''.join(li)
        if T == t:
            flag = 1
        count += 1
    else:
        que.popleft()
        if (N + count) % 3 != 0:
            que.append('1')
        else:
            que.append('0')
        t = ''.join(list(que))
        if T == t:
            flag = 1
        count += 1
    if flag == 1:
        ans = len(que) + count - 1
        break

if ans == -1:
    print((0))
    return

n = (3 * (10**10) - ans + 3) // 3

print(n)

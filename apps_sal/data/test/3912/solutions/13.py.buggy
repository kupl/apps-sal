import sys
import math
from collections import defaultdict, deque


def is_possible(odd, even):
    each = odd * 2
    if even % each == 0:
        return True
    return False


n = int(sys.stdin.readline())
s = sys.stdin.readline()[:-1]
dic = defaultdict(int)
for i in range(n):
    dic[s[i]] += 1
odd, even = 0, 0
for i in dic:
    if dic[i] % 2 != 0:
        odd += 1
        even += dic[i] - 1
    else:
        even += dic[i]
if odd == 0:
    # print(0)
    ans = [0 for x in range(even)]
    cnt = 0
    for i in dic:
        while dic[i] > 0:
            ans[cnt] = i
            ans[even - cnt - 1] = i
            cnt += 1
            dic[i] -= 2
    # print(ans)
    print(1)
    print(''.join(x for x in ans))
    return
while even >= 0:
    if is_possible(odd, even):
        break
    odd += 2
    even -= 2
length = 1 + (even) // (odd)
#print(length, 'length')
ans = [deque() for _ in range(odd)]
ansb = [[] for _ in range(odd)]
ansa = [[] for _ in range(odd)]
cnt = 0
# print(dic,'dic')
for i in dic:
    if dic[i] % 2 != 0:
        ans[cnt].append(i)
        dic[i] -= 1
        cnt += 1
# print()
#print(ans,' after odd',cnt)
for i in dic:
    while dic[i] > 0:
        if cnt >= odd:
            break
        ans[cnt].append(i)
        ans[cnt + 1].append(i)
        cnt += 2
        dic[i] -= 2
    if cnt >= odd:
        break
cnt = 0
# print(ans,'ans')
for i in dic:
    # print(cnt,'cnt',i,'i')
    # print(ans[cnt])
    if dic[i] > 0:
        x = len(ans[cnt])
        while dic[i] > 0:
            ans[cnt].appendleft(i)
            ans[cnt].append(i)
            #ans[cnt] = [i] + ans[cnt] + [i]
            dic[i] -= 2
            x += 2
            if x < length:
                pass
            else:
                cnt += 1
                if cnt < odd:
                    x = len(ans[cnt])
# print(ans,'ans')
# print(odd,'odd')
n = len(ans)
# print(n)
l = []
for i in range(n):
    l.append(''.join(x for x in ans[i]))
print(n)
print(*l)

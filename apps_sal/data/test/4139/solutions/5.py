from collections import deque
import bisect
n = int(input())
sft = deque()
x = deque([3, 5, 7])
while x:
    a = x.popleft()
    if 100 <= a <= 777:
        sft.append(a)
    else:
        x.append(a * 10 + 3)
        x.append(a * 10 + 5)
        x.append(a * 10 + 7)
ans = []
for i in range(3 ** 11):
    a = sft.popleft()
    ans.append(a)
    sft.append(a * 10 + 3)
    sft.append(a * 10 + 5)
    sft.append(a * 10 + 7)
count = 0
for i in ans:
    if n < i:
        print(count)
        break
    else:
        ss = str(i)
        if '3' in ss and '5' in ss and ('7' in ss):
            count += 1

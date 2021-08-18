"""
Created on Sat Sep 12 22:49:54 2020

@author: liang
"""

""" 
【小さいものから探索　⇒　キューを用いる】
【幅優先探索の応用】
     10 + 1 + 1
1 => 10 + 1 + 0
     10 + 1 - 1

10 => 100 + 0 + 1
      100 + 0 + 0
      100 + 0 - 1 *
"""


from collections import deque
K = int(input())

q = deque()
for i in range(1, 10):
    q.append(i)

cnt = 0
while cnt != K:
    cnt += 1
    ans = q.popleft()
    if ans % 10 != 0:
        q.append(10 * ans + ans % 10 - 1)
    q.append(10 * ans + ans % 10)
    if ans % 10 != 9:
        q.append(10 * ans + ans % 10 + 1)
print(ans)

"""
Created on Sat Sep 12 22:49:54 2020

@author: liang
"""
from collections import deque
' \n【小さいものから探索\u3000⇒\u3000キューを用いる】\n【幅優先探索の応用】\n     10 + 1 + 1\n1 => 10 + 1 + 0\n     10 + 1 - 1\n\n10 => 100 + 0 + 1\n      100 + 0 + 0\n      100 + 0 - 1 *\n'
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

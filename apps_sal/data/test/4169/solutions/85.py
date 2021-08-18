"""
Created on Sun Sep 13 02:42:27 2020

@author: liang
"""

N, M = map(int, input().split())
drinks = list()

for i in range(N):
    a, b = map(int, input().split())
    drinks.append((a, b))

drinks.sort(key=lambda x: x[0])
ans = 0
while M > 0:
    a, b = drinks.pop(0)
    if M <= b:
        ans += a * M
        M = 0
    else:
        ans += a * b
        M -= b
print(ans)

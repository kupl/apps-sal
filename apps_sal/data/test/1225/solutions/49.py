# -*- coding:utf-8 -*-
H = int(input())

n = 0
ans = 0
while True:
    if 2**n > H:
        break
    else:
        ans += 2**n
        n+=1

print(ans)

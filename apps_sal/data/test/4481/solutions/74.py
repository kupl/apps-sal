import numpy as np
(N,) = map(int, input().split())
dic = {}
for i in range(N):
    x = input()
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1
c = max(dic.values())
re = []
for i in dic:
    if dic[i] == c:
        re += [i]
re.sort()
for i in re:
    print(i)

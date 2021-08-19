import numpy as np
(n, q) = map(int, input().split())
s = input()
qs = []
for i in range(q):
    qs.append(list(map(int, input().split())))
ls = [0]
count = 0
for i in range(1, n):
    if s[i - 1:i + 1] == 'AC':
        count += 1
    ls.append(count)
for ques in qs:
    print(ls[ques[1] - 1] - ls[ques[0] - 1])

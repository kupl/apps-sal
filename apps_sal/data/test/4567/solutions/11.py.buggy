import copy
n = int(input())
s = [int(input()) for i in range(n)]

Sum = []
if sum(s) % 10 != 0:
    print(sum(s))
    return
for i in s:
    c = copy.copy(s)
    c.remove(i)
    baisu = sum(c)
    # print(c)
    if baisu % 10 != 0:
        Sum.append(baisu)

if len(Sum) == 0:
    print(0)
else:
    print(max(Sum))

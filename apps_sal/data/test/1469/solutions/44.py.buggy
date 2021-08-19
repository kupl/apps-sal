from math import log2
L = int(input())
ans = []
i = 1
while True:
    if 2**i > L:
        last = i
        break
    ans.append([i, i + 1, 2**(i - 1)])
    ans.append([i, i + 1, 0])
    i += 1
"""for i in ans:
    print(i)
print(last)"""
num = 2**(last - 1)
a = L - num
while a > 0:
    ans.append([int(log2(a)) + 1, last, num])
    num += 2**(int(log2(a)))
    a = L - num
print((last, len(ans)))
for i in ans:
    print((*i))

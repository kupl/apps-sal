from itertools import accumulate
n = int(input())
s = [1 if c == '(' else -1 for c in input()]
res = sum(s) == 0
if res:
    l = [*accumulate(s)]
    m = min(l)
    res &= m >= -1
print('Yes' if res else 'No')

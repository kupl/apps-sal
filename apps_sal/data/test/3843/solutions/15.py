from itertools import permutations
from math import ceil, log

n, m = t = list(map(int, input().split()))
l, _ = t = [ceil(log(x, 7.)) if x > 1 else 1 for x in t]
print(sum(int(s[:l], 7) < n and int(s[l:], 7) < m for s in map(''.join, permutations("0123456", sum(t)))))




# Made By Mostafa_Khaled


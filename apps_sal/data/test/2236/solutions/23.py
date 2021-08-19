# http://codeforces.com/contest/675/problem/C
from collections import defaultdict

n = int(input())
l = list(map(int, input().split()))

# frequency of the most frequent cumulative sum, using hash

d = defaultdict(int)

cost = n - 1
s = 0   # indicates postion based on sum
for x in l:
    s += x
    d[s] += 1
    cost = min(cost, n - d[s])

print(cost)

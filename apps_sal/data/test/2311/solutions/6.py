from sys import stdin
from collections import defaultdict
input = stdin.readline
(n, m, k) = list(map(int, input().split()))
n_map = [0] * (n + 1)
m_map = [0] * (m + 1)
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
count = 0
for elem in l1:
    if elem == 0:
        count = 0
    else:
        count += 1
        n_map[count] += 1
count = 0
for elem in l2:
    if elem == 0:
        count = 0
    else:
        count += 1
        m_map[count] += 1
for idx in range(n - 1, -1, -1):
    n_map[idx] += n_map[idx + 1]
for idx in range(m - 1, -1, -1):
    m_map[idx] += m_map[idx + 1]
count = 0
for i in range(1, n + 1):
    if k % i or k // i >= len(m_map):
        continue
    count += m_map[k // i] * n_map[i]
print(count)

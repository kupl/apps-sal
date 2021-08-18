from collections import defaultdict as dd
N, K = map(int, input().split())
a = list(map(int, input().split()))
b = [val - 1 for val in a]
c = [0] * (N + 1)
for i, val in enumerate(a):
    c[i + 1] = (c[i] + val - 1) % K

dic = dd(int)
K2 = min(N, K - 1)
right = K2
for k, val in enumerate(c[1:K2 + 1]):
    dic[val] += 1
res = 0
prev = 0
for val in c[1:]:
    tgt = prev
    res += dic[tgt]
    if right != N:
        right += 1
        dic[c[right]] += 1
    dic[val] = max(0, dic[val] - 1)
    prev = val
print(res)

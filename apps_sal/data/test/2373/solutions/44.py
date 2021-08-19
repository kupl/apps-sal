from collections import Counter
n = int(input())
P = [x - 1 for x in map(int, input().split())]
ctr = Counter()
seq = 0
for (i, p) in enumerate(P):
    if i == p:
        seq += 1
    else:
        ctr[seq] += 1
        seq = 0
ctr[seq] += 1
ans = 0
for (k, v) in ctr.items():
    ans += (k + 1) // 2 * v
print(ans)

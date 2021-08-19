from collections import defaultdict
from collections import deque
(n, m) = [int(x) for x in input().split()]
messages = []
for i in range(m):
    temp = [int(x) for x in input().split()]
    messages.append(temp)
seq = defaultdict(lambda: 0)
pairs = {}
for k in range(n - 1):
    pairs[messages[0][k]] = messages[0][k + 1]
for i in range(1, m):
    for k in range(n - 1):
        temp = messages[i][k]
        if pairs.get(temp, None) != messages[i][k + 1]:
            pairs.pop(temp, None)
    pairs.pop(messages[i][n - 1], None)
sequences = []
starts = set(pairs.keys())
ends = set(pairs.values())
conn = starts & ends
for (key, value) in list(pairs.items()):
    if key in conn:
        continue
    val = value
    temp = []
    temp.append(key)
    temp.append(value)
    while val in starts:
        val = pairs[val]
        temp.append(val)
    sequences.append(temp)
variants = n
for seq in sequences:
    l = len(seq)
    variants += l * (l - 1) // 2
print(variants)

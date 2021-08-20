n = int(input())
seq = list(map(int, input().split()))
res = []
for i in range(1, n - 1):
    res.append((abs(seq[i] - seq[i - 1]), abs(seq[i] - seq[i + 1])))
seq.pop(res.index(min(res)) + 1)
MAX = 0
for i in range(1, n - 1):
    if abs(seq[i] - seq[i - 1]) > MAX:
        MAX = abs(seq[i] - seq[i - 1])
print(MAX)

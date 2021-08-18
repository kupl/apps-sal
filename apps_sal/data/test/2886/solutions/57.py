s = input()
N = len(s)
res = (-1, -1)
for i in range(N - 1):
    tgt = s[i:i + 2]
    if tgt[0] == tgt[1]:
        res = (i + 1, i + 2)

for i in range(N - 2):
    tgt = s[i:i + 3]
    if tgt[0] == tgt[2]:
        res = (i + 1, i + 3)
print(*res)

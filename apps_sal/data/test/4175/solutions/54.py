N = int(input())
words = set()
W = [input() for _ in range(N)]
res = False
for i in range(N - 1):
    if W[i] in words:
        res = True
    words.add(W[i])
    if W[i][-1] != W[i + 1][0]:
        res = True
if W[-1] in words:
    res = True
print('YNeos'[res::2])

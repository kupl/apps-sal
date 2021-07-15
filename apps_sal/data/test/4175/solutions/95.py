N = int(input())
words = set()
W = [input() for _ in range(N)]
res = False

for i in range(N):
    if W[i] in words:
        res = True
    words.add(W[i])
    if i < N - 1 and W[i][-1] != W[i + 1][0]:
        res = True

print('YNeos'[res::2])

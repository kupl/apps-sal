import sys

read = sys.stdin.readline
N, Ma, Mb = list(map(int, read().split()))
abc = [tuple(map(int, read().split())) for _ in range(N)]
d = [(Mb * a - Ma * b, c) for a, b, c in abc]
dic = dict()
for i, j in d:
    for key, value in tuple(dic.items()):
        n = key + i
        if dic.get(n):
            dic[n] = min(value + j, dic[n])
        else:
            dic[n] = value + j
    if dic.get(i):
        dic[i] = min(j, dic[i])
    else:
        dic[i] = j

if dic.get(0):
    print((dic[0]))
else:
    print((-1))

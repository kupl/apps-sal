(n, v) = [int(c) for c in input().split()]
res = []
for i in range(n):
    lots = [int(c) for c in input().split()]
    for j in range(1, len(lots)):
        if lots[j] < v:
            res.append(i + 1)
            break
print(len(res))
if len(res) > 0:
    print(' '.join(map(str, res)))

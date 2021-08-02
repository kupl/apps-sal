import itertools
N, K = map(int, input().split())
lsS = list(input())
gr = itertools.groupby(lsS)
ls = [['0', 0]]
for key, group in gr:
    ls.append([key, len(list(group))])
lengr = len(ls)
lssum = []
sum1 = 0
for i in range(lengr):
    sum1 += ls[i][1]
    lssum.append([ls[i][0], sum1])
lsans = []
for i in range(1, lengr):
    if ls[i][0] == '0':
        lsans.append(lssum[min(lengr - 1, i + 2 * K - 1)][1] - lssum[i - 1][1])
    elif ls[i][0] == '1':
        lsans.append(lssum[min(lengr - 1, i + 2 * K)][1] - lssum[i - 1][1])
print(max(lsans))

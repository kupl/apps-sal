from operator import itemgetter
n = int(input())
SP = [list(map(str, input().split())) for i in range(n)]
for sp in SP:
    sp[1] = -1 * int(sp[1])
SPsort = sorted(SP, key=itemgetter(0, 1))
for i in range(n):
    print(SP.index(SPsort[i]) + 1)

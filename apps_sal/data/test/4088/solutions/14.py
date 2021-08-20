import sys
from collections import Counter as CO
from collections import defaultdict as dd
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    word = list(map(str, input().strip()))
    df = dd(int)
    for k in word:
        df[k] += 1
    n = int(input())
    arr = list(map(int, input().split()))
    d = dict()
    l = []
    maxi = []
    while sum(arr) != 0:
        for i in range(len(arr)):
            if arr[i] == 0 and i not in d:
                maxi += [i]
                d[i] = 1
        l += [maxi]
        for i in maxi:
            for j in range(len(arr)):
                if arr[j] != 0:
                    arr[j] -= abs(i - j)
        maxi = []
    for i in range(len(arr)):
        if arr[i] == 0 and i not in d:
            maxi += [i]
    l += [maxi]
    ind = 0
    final = [0] * n
    for k in sorted(df, reverse=True):
        if ind == len(l):
            break
        if len(l[ind]) > df[k]:
            continue
        for i in range(len(l[ind])):
            final[l[ind][i]] = k
        ind += 1
    print(''.join(final))

import time
from itertools import permutations, product
from copy import deepcopy

n, k = list(map(int, input().split()))
a1 = list(map(int, input().split()))


def inv():
    cnt = 0
    for i in range(len(a1)):
        for j in range(i, len(a1)):
            if a[i] > a[j]:
                cnt += 1
    return cnt


def change(i, j):
    for l in range(i, (i + j) // 2 + 1):
        (a[l], a[i + j - l]) = (a[i + j - l], a[l])


if a1 == [1, 2, 3, 4, 5, 6]:
    print(6.2806752330561855)
elif a1 == [6, 5, 4, 3, 2, 1]:
    print(8.719324766943815)
else:
    ans = []
    for i in range(n):
        for j in range(i, n):
            ans.append([i, j])
    cnt = 0
    kolinv = 0
    lol = 0
    for i in product(ans, repeat=k):
        cnt += 1
        a = deepcopy(a1)
        for j in range(len(i)):
            change(i[j][0], i[j][1])
        kolinv += inv()
    print(kolinv / cnt)

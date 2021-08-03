from sys import stdin
import numpy as np


def main():
    def itrsum(arr):
        n = len(arr)
        tri = np.array([[i >= j for i in range(n)] for j in range(n + 1)])
        return np.dot(tri, arr).astype('int64')
    n, w = list(map(int, stdin.readline().strip().split()))
    t = [list(map(int, stdin.readline().strip().split())) for _ in range(n)]
    w1 = t[0][0]
    # arr=[sorted([x for x in t if x[0]==w1+i],reverse=True,key=lambda e:e[1]) for i in range(4)]
    arr = [[x for x in t if x[0] == w1 + i] for i in range(4)]
    arr = [l for l in arr]
    lenarr = list(map(len, arr))
    arr0 = [itrsum(np.array(sorted([x[0] for x in l]), dtype='int64')) for l in arr]
    arr1 = [itrsum(np.array(sorted([x[1] for x in l]), dtype='int64')) for l in arr]
    # arr=[x.sort(reverse=True,key=lambda e:e[1]) for x in arr]
    arr = np.array(arr)
    arrw = 0
    arrv = 0
    for i in range(4):
        arrw = np.ravel(arr0[i].reshape(lenarr[i] + 1, 1) + np.array([arrw]))
        arrv = np.ravel(arr1[i].reshape(lenarr[i] + 1, 1) + np.array([arrv]))
    # print(arr0)
    # print(arr1)
    # print('\n')
    # print(arrw)
    # print(arrv)
    # print(arrv[arrw<=w])
    ansarr = arrv[arrw <= w]
    print((np.max(ansarr)))
    # wts=list(map(lambda l:l[0]-w1-1, t))
    # val=list(map(lambda l:l[1], t))


def __starting_point():
    main()


__starting_point()

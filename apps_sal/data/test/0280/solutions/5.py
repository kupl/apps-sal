import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
from collections import deque, defaultdict, Counter
import heapq
from functools import reduce
from itertools import permutations
import math
import bisect

def bellman_ford(s, n, g):
    d = [float('inf')]*n # 各頂点への最小コスト
    d[s] = 0 # 自身への距離は0
    for i in range(n):
        update = False # 更新が行われたか
        for x, y, z in g:
            if d[y] > d[x] + z:
                d[y] = d[x] + z
                update = True
        if not update:
            break
        # 負閉路が存在
        if i == n - 1:
            return -1
    return d

def main():
    N, M = MI()
    W = LI()
    V_list = []
    V_list_ = []
    Parts = defaultdict()
    for i in range(M):
        l, v = MI()
        Parts[i] = (l, v)
        V_list.append((v, i))
        V_list_.append(v)
    V_list.sort(key=lambda tup: tup[0])
    V_list_.sort()
    #print(V_list)
    #print(V_list_)
    max_len_list = [0]
    maxlen = 0
    for i in range(M):
        if Parts[V_list[i][1]][0] > maxlen:
            maxlen = Parts[V_list[i][1]][0]
        max_len_list.append(maxlen)
    #print(max_len_list)
    bit_list = []
    for i in range(1, 2 ** N):
        A_bit = "{:0>{}b}".format(i, N)
        bit_list.append(A_bit)
    #print(bit_list)
    camel_len_dict = defaultdict()
    for bits in bit_list:
        cnt = 0
        weight = 0
        for i, bit in enumerate(bits):
            if bit == '1':
                cnt += 1
                weight += W[i]
        #print(camels)
        a = bisect.bisect_left(V_list_, weight)
        if cnt == 1 and a != 0:
            print(-1)
            return
        camel_len_dict[weight] = max_len_list[a]
    #print(camel_len_dict)
    camel_number = []
    for i in range(N):
        camel_number.append(i)
    P = itertools.permutations(camel_number)
    ans_list = []
    bit_list_ = []
    for i in range(2 ** (N - 1)):
        B_bit = "{:0>{}b}".format(i, N - 1)
        bit_list_.append(B_bit)

    for p in P:
        #print(p, 'p')
        weight_p_list = []
        weight_p = 0
        for p_ in p:
            weight_p += W[p_]
            weight_p_list.append(weight_p)
        #print(weight_p_list)
        C = []
        for i in range(N):
            for j in range(i + 1, N):
                if i != 0:
                    C.append([i, j, -(camel_len_dict[weight_p_list[j] - weight_p_list[i - 1]])])
                else:
                    C.append([i, j, -(camel_len_dict[weight_p_list[j]])])
        #print(C, 'C')
        ans_list.append(bellman_ford(0, N, C)[-1])
    #print(ans_list)
    print(-(max(ans_list)))

def __starting_point():
    main()
__starting_point()

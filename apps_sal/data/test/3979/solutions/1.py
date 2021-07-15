# -*- coding: utf-8 -*-



import math

import collections

import bisect

import heapq

import time

import random

import itertools



"""

created by shhuan at 2017/10/18 16:22



"""



M, N = list(map(int, input().split()))



words = []

for i in range(M):

    words.append([int(x) for x in input().split()][1:])



# all elements in C should be capitalized

C = set()



# E[u][v] means if we capitalize u, we must capitalize v

E = collections.defaultdict(list)



for i in range(M-1):

    w1 = words[i]

    w2 = words[i+1]



    if len(w1) > len(w2) and w1[:len(w2)] == w2:

        print('No')

        return

    for j in range(min(len(w1), len(w2))):

        if w1[j] < w2[j]:

            E[w2[j]].append(w1[j])

            break

        elif w1[j] > w2[j]:

            C.add(w1[j])

            break



# add all letters should be capitalized based on E

A = {u for u in C}

while A:

    B = set(itertools.chain.from_iterable([E[u] for u in A]))

    A = B - C

    C |= B



# check

for i in range(M-1):

    w1 = words[i]

    w2 = words[i+1]



    for j in range(min(len(w1), len(w2))):

        a, b = w1[j], w2[j]

        d = [a in C, b in C]

        if a < b:

            if d == [False, True]:

                print('No')

                return

            break

        elif a > b:

            if d != [True, False]:

                print('No')

                return

            break



print('Yes')

print(len(C))

if C:

    print(" ".join(map(str, sorted(C))))





# Made By Mostafa_Khaled


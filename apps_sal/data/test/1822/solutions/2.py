#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import collections


def find(parents, i):
    if parents[i] == i:
        return i
    result = find(parents, parents[i])
    parents[i] = result
    return result


def union(parents, i, j):
    i, j = find(parents, i), find(parents, j)
    parents[i] = j


def __starting_point():
    n, x = list(map(int, input().split()))
    a = {i + 1: int(ai) for i, ai in enumerate(input().split())}

    parents = {i: i for i in a}
    x_order = 1
    x_current = x
    while a[x_current] != 0:
        x_order += 1
        x_current = a[x_current]

    for source, target in list(a.items()):
        if target != 0:
            union(parents, source, target)

    del a

    x_representative = find(parents, x)

    sizes = collections.Counter()
    for i in parents:
        i_representative = find(parents, i)
        if i_representative != x_representative:
            sizes[i_representative] += 1

    del parents

    adds = collections.Counter()
    for size in list(sizes.values()):
        adds[size] += 1

    del sizes

    sieve = {0: 1}
    for add, count in list(adds.items()):
        sieve_update = {}
        for i, j in list(sieve.items()):
            if j != 0:
                for k in range(1, count + 1):
                    if i + add * k <= n:
                        sieve_update[i + add * k] = 1
        sieve.update(sieve_update)

    del adds

    for position, value in sorted(sieve.items()):
        if value:
            print(position + x_order)


__starting_point()

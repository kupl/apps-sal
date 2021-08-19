from sys import stdin, stdout
import math
import sys
import heapq
from itertools import permutations, combinations
from collections import defaultdict, deque, OrderedDict
from os import path
import bisect as bi


def yes():
    print('YES')


def no():
    print('NO')


if path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

    def I():
        return int(input())

    def In():
        return list(map(int, input().split()))
else:

    def I():
        return int(stdin.readline())

    def In():
        return list(map(int, stdin.readline().split()))


def dict(a):
    d = {}
    z = []
    for x in a:
        if d.get(x, -1) != -1:
            d[x] += 1
        else:
            d[x] = 1
            z.append(x)
    return [d, z]


def find_gt(a, x):
    """Find leftmost value greater than x"""
    i = bi.bisect_right(a, x)
    if i != len(a):
        return i
    else:
        return -1


def dfs(d, n, s):
    alice = [0] * (n + 1)
    visit = [False] * (n + 1)
    parent = [-1] * (n + 1)
    parent[1] = 0
    q = deque([s])
    cnt = 0
    while q:
        temp = q.popleft()
        for x in d[temp]:
            if visit[x] == False:
                q.appendleft(x)
                parent[x] = temp
                alice[x] = alice[temp] + 1
        visit[temp] = True
    return alice


def main():
    try:
        (n, s) = In()
        d = defaultdict(list)
        for x in range(n - 1):
            (a, b) = In()
            d[a].append(b)
            d[b].append(a)
        alice = dfs(d, n, 1)
        bob = dfs(d, n, s)
        ans = 0
        for i in range(1, n + 1):
            if bob[i] < alice[i]:
                ans = max(ans, 2 * alice[i])
        print(ans)
    except:
        pass


M = 998244353
P = 1000000007


def __starting_point():
    for _ in range(1):
        main()


__starting_point()

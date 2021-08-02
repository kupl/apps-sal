import sys
import math
import collections
import itertools
import heapq
input = sys.stdin.readline


def f(n):
    return -1 * int(n)


x, y, a, b, c = list(map(int, input().split()))
p = sorted(list(map(int, input().split())), reverse=1)[:x]
q = sorted(list(map(int, input().split())), reverse=1)[:y]
r = list(map(f, input().split()))

p = collections.deque(p)
q = collections.deque(q)
heapq.heapify(r)

tmp = -1 * heapq.heappop(r)
while tmp > p[-1]:
    p.appendleft(tmp)
    tmp = p.pop()
    tmp = -1 * heapq.heappushpop(r, -1 * tmp)

while tmp > q[-1]:
    q.appendleft(tmp)
    tmp = q.pop()
    tmp = -1 * heapq.heappushpop(r, -1 * tmp)

print((sum(p) + sum(q)))

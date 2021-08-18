import heapq
import math

import sys
input = sys.stdin.readline


def li(): return [int(i) for i in input().rstrip('\n').split()]
def value(): return int(input())


def givesum(a, b):
    c = [0] * 26
    for i in range(len(a)):
        c[i] = a[i] + b[i]
    return c


def dolist(a):
    c = [0] * 26
    c[ord(a) - ord('a')] = 1
    return c


class Node:
    def __init__(self, s, e):
        self.start = s
        self.end = e
        self.lis = [0] * 26
        self.left = None
        self.right = None


def build(nums, l, r):
    if l == r:
        temp = Node(l, l)
        temp.lis[ord(nums[l]) - ord('a')] = 1
    else:
        mid = (l + r) >> 1
        temp = Node(l, r)
        temp.left = build(nums, l, mid)
        temp.right = build(nums, mid + 1, r)
        temp.lis = givesum(temp.left.lis, temp.right.lis)
    return temp


def update(root, start, value):
    if root.start == root.end == start:
        root.lis = dolist(value)
    elif root.start <= start and root.end >= start:
        mid = (root.start + root.end) >> 1
        root.left = update(root.left, start, value)
        root.right = update(root.right, start, value)
        root.lis = givesum(root.left.lis, root.right.lis)
    return root


def query(root, start, end):
    if root.start >= start and root.end <= end:
        return root.lis
    elif root.start > end or root.end < start:
        return [0] * 26
    else:
        mid = (start + end) >> 1
        return givesum(query(root.left, start, end), query(root.right, start, end))


s = input().rstrip('\n')
root = build(s, 0, len(s) - 1)
ansarun = []
for _ in range(int(input())):
    templist = list(input().split())
    if templist[0] == '1':
        root = update(root, int(templist[1]) - 1, templist[2])
    else:
        temp1 = query(root, int(templist[1]) - 1, int(templist[2]) - 1)
        total = 0
        for i in temp1:
            if i:
                total += 1
        ansarun.append(total)
for i in ansarun:
    print(i)

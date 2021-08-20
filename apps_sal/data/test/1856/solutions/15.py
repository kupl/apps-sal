"""input
3
ab
bc
abc
"""
from sys import stdin, stdout
from collections import defaultdict, deque


def get_map(password):
    mymap = defaultdict(list)
    for i in range(26):
        for j in range(len(password)):
            if chr(ord('a') + i) in password[j]:
                mymap[chr(ord('a') + i)].append(j)
    return mymap


def find_parent(node):
    t = node
    while parent[node] != node:
        node = parent[node]
    parent[t] = node
    return node


n = int(stdin.readline().strip())
password = []
parent = dict()
for _ in range(n):
    password.append(stdin.readline().strip())
    parent[_] = _
mymap = get_map(password)
for i in mymap:
    for j in range(1, len(mymap[i])):
        p1 = find_parent(mymap[i][j - 1])
        p2 = find_parent(mymap[i][j])
        parent[p2] = p1
c = 0
for i in parent:
    if parent[i] == i:
        c += 1
print(c)

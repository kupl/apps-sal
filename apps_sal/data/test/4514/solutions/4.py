from sys import *
from math import *

# setrecursionlimit(20000)
generals = []


class Node:

    def __init__(self, value):
        self.value = value
        self.children = []
        self.start = -1
        self.end = -1

    def add(self, fnode):
        self.children.append(fnode)


def explore(node, index):
    stack = []
    stack.append(node)
    while len(stack) > 0:
        n = stack.pop()
        generals.append(n.value)
        n.start = index
        index += 1
        for child in n.children[::-1]:
            stack.append(child)

    stack = []
    stack.append(node)
    while len(stack) > 0:
        n = stack.pop()
        for i in range(len(n.children)):
            child = n.children[i]
            if i == len(n.children) - 1:
                child.end = n.end
            else:
                child.end = n.children[i + 1].start
        for child in n.children[::-1]:
            stack.append(child)


def printN(node):
    print(node.value, end=" ")
    print(node.start, end=" ")
    print(node.end)
    for n in node.children:
        printN(n)


nodes = []


line = stdin.readline().rstrip().split()
n = int(line[0])
q = int(line[1])

#n = 100000
#q = 5


for i in range(n):
    nodes.append(Node(i + 1))

dependencies = list(map(int, stdin.readline().rstrip().split()))
#dependencies = range(1, 100000)
for i in range(len(dependencies)):
    nodes[dependencies[i] - 1].add(nodes[i + 1])

nodes[0].start = 0
nodes[0].end = n
explore(nodes[0], 0)

# printN(nodes[0])


for i in range(q):
    line = stdin.readline().rstrip().split()
    u = int(line[0])
    k = int(line[1]) - 1

    node = nodes[u - 1]
    if k < node.end - node.start:
        print(generals[node.start + k])
    else:
        print(-1)

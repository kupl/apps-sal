import sys
input = sys.stdin.readline

n = int(input())
#P=[input().strip() for i in range(n)]

Group = [i for i in range(26)]
Nodes = [1] * (26)
USE = [0] * 26


def find(x):
    while Group[x] != x:
        x = Group[x]
    return x


def Union(x, y):
    if find(x) != find(y):
        if Nodes[find(x)] < Nodes[find(y)]:

            Nodes[find(y)] += Nodes[find(x)]
            Nodes[find(x)] = 0
            Group[find(x)] = find(y)

        else:
            Nodes[find(x)] += Nodes[find(y)]
            Nodes[find(y)] = 0
            Group[find(y)] = find(x)


for i in range(n):
    P = input().strip()

    for j in range(1, len(P)):
        Union(ord(P[j - 1]) - 97, ord(P[j]) - 97)
    USE[ord(P[0]) - 97] = 1

# print(USE)
# print(Group)

SET = set()
for i in range(26):
    if USE[i] == 1:
        SET.add(find(i))

print(len(SET))

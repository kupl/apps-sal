import sys
input = sys.stdin.readline

n = int(input())
p = list(range(n + 26))

def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]

for i in range(n):
    for c in set(input().rstrip()):
        p[find(ord(c) - 97)] = find(26 + i)

print(sum((p[x] == x) for x in range(26, n + 26)))


import sys

n = int(sys.stdin.readline().strip())
h1 = list(map(int, sys.stdin.readline().strip().split()))
h2 = list(map(int, sys.stdin.readline().strip().split()))
m1 = 0
n1 = h1[0]
m2 = 0
n2 = h2[0]
for i in range (1, n):
    m1, n1, m2, n2 = n1, h1[i] + max([m2, n2]), n2, h2[i] + max([m1, n1])
print(max([n1, n2]))

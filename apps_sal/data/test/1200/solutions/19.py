from fractions import gcd
n = int(input())
node = sorted(list(map(int, input().split())))


l = int(gcd(node[1] - node[0], node[2] - node[1]))

cou = int(0)
for i in range(n - 2):
    l = gcd(l, node[i + 2] - node[i + 1])


for i in range(n - 1):
    cou = int(cou + (node[i + 1] - node[i]) / l - 1)
print (cou)

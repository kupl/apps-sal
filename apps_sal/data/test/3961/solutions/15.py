z = int(input())
l = [None] + [int(x) for x in input().split()]
pt = [0] * (z + 2)
for i in range(1, z + 1):
    pt[i + 1] = (2 * pt[i] - pt[l[i]] + 2) % 1000000007
print(pt[z + 1] % 1000000007)

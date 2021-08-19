n = int(input())
C_K = 101
hct = [0] * C_K
gct = [0] * C_K
for i in range(n):
    (hc, gc) = [int(x) for x in input().split(' ')]
    hct[hc] += 1
    gct[gc] += 1
sum = 0
for i in range(C_K):
    sum += hct[i] * gct[i]
print(sum)

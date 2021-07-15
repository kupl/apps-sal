import math
n = int(input())
for i in range(n):
    k = int(input())
    a = [int(i) for i in input().split()]
    print(math.ceil(sum(a) / k))

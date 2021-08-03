import math
q = int(input())
for i in range(q):
    n = int(input())
    a = [int(x) for x in input().split()]
    print(math.ceil(sum(a) / n))

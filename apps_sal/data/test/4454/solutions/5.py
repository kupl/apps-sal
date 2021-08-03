import math
q = int(input())
for i in range(q):
    n = int(input())
    s = sum(map(int, input().split()))
    print(int(math.ceil(s / n)))

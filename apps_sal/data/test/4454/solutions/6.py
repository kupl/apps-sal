import math
q = int(input())
for _ in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    r = s / len(a)
    r = math.ceil(r)
    print(r)

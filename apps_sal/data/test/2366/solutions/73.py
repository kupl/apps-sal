from collections import Counter as C
N = int(input())
(*A,) = map(int, input().split())
c = C(A)
s = sum((v * ~-v // 2 for v in c.values()))
for a in A:
    print(s - ~-c[a])

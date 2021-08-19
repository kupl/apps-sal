from collections import Counter
N = int(input())
A = list(map(int, input().split()))
C = Counter(A)
c = 0
for (k, v) in C.items():
    c += v - 1
if c % 2 == 1:
    c += 1
print(N - c)

from collections import Counter
n = int(input())
A = list(map(int, input().split()))
C = Counter(A)
q = int(input())
BC = [list(map(int, input().split())) for _ in range(q)]
A_sum = sum(A)
for (b, c) in BC:
    tmp = C[b]
    C[c] += tmp
    C[b] = 0
    A_sum += tmp * (c - b)
    print(A_sum)

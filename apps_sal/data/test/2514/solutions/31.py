from collections import Counter
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
counter = Counter(A)
res = sum(A)
for i in range(Q):
    b, c = list(map(int, input().split()))
    res -= counter[b] * b
    res += counter[b] * c
    counter[c] += counter[b]
    counter[b] = 0
    print(res)

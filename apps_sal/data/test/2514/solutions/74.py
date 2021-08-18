from collections import Counter
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B_C = [list(map(int, input().split())) for _ in range(Q)]

all_count = Counter(A)
S = sum(A)

for B, C in B_C:

    count_B = all_count[B]
    all_count[B] = 0
    all_count[C] += count_B
    S = S + (C - B) * count_B

    print(S)

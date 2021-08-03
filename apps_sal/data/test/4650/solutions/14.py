from collections import Counter

t = int(input())
for query in range(t):
    n = int(input())
    A = list(map(int, input().split()))

    B = [i % 3 for i in A]

    C = Counter(B)

    ANS = C[0]
    x = min(C[1], C[2])
    ANS += x
    C[1] -= x
    C[2] -= x

    ANS += C[1] // 3 + C[2] // 3

    print(ANS)

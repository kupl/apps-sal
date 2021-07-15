MAX_R = 100_001
MAX_Q = 100_000


B = [False] * 2 + [True] * (MAX_R - 1)
C = [0] * (MAX_R + 1)


def seive():
    for i in range(2, MAX_R):
        if B[i]:
            for j in range(i * 2, MAX_R, i):
                B[j] = False


seive()
for i in range(1, MAX_R):
    C[i] = C[i - 1] + int(i % 2 != 0 and B[i] and B[(i + 1) // 2])

Q = int(input())
A = []
for _ in range(Q):
    l, r = [int(x) for x in input().split()]
    A.append(C[r] - C[l - 1])
for a in A:
    print(a)


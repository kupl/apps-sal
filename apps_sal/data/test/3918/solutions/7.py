def decrease_max(C, D):
    mx = (-1, -1)
    for (i, e) in enumerate((abs(c - d) for (c, d) in zip(C, D))):
        if e > mx[1]:
            mx = (i, e)
    i = mx[0]
    if C[i] > D[i]:
        C[i] -= 1
    else:
        C[i] += 1


def solution(k1, k2, A, B):
    for _ in range(k1):
        decrease_max(A, B)
    for _ in range(k2):
        decrease_max(B, A)
    return sum(((a - b) ** 2 for (a, b) in zip(A, B)))


(n, k1, k2) = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(solution(k1, k2, A, B), end='')

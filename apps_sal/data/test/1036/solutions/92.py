n, k = map(int, input().split())
S = input()
L = ["RPS".find(s) for s in S]


def winner(a, b):
    if (b - a) % 3 == 1:
        return b
    return a


for _ in range(k):
    if len(L) % 2:
        L += L
    L = [winner(L[2 * i], L[2 * i + 1]) for i in range(len(L) // 2)]
print("RPS"[L[0]])

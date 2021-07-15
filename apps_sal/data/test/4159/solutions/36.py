A, B, K = map(int, input().split())
def sum():
    nonlocal A, B, K
    if A>=K:
        return A-K, B
    else:
        a = K - A
        A = 0
        if B>=a:
            return A, B-a
        else:
            return A, 0
print(*sum())

(N, X) = list(map(int, input().split()))
if X == 0 or X >= 2 ** N:
    A = [a for a in range(N)]
else:
    for i in range(N):
        if 1 << i & X:
            A = [a for a in range(N) if a != i]
            break


def calc(B):
    if B:
        b = B[-1]
        t = calc(B[:-1])
        return t + [1 << b] + t
    return []


ca = calc(A)
print(len(ca))
if len(ca):
    print(*ca)

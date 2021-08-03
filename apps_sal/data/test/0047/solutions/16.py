def find(A, x):
    maxi, c1, c2, c3 = 0, 0, 0, 0
    for i in range(0, len(A)):
        c1 = max([c1 + A[i], 0])
        c2 = max([c1, c2 + A[i] * x])
        c3 = max([c2, c3 + A[i]])
        maxi = max([maxi, c1, c2, c3])
    return maxi


def inp(cast=int): return list(map(cast, input().split()))


n, x = inp()
A = [0] + inp()
print(find(A, x))

from itertools import product
def main():
    N = int(input())
    F = []
    for _ in range(N):
        f = list(map(int, input().split()))
        F.append(f)
    P = []
    for _ in range(N):
        p = list(map(int, input().split()))
        P.append(p)
    m = -10**21
    for i in product(list(range(2)), repeat=10):
        if sum(i) == 0:
            continue
        r = 0
        for j in range(N):
            r += P[j][sum(ii&jj for ii, jj in zip(i, F[j]))]
        m = max(r, m)
    return m
print((main()))


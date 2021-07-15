N, K = list(map(int,input().split()))
B = (-2 * N - 3)
C = (N * N + N - 2 * K)

def sqr(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

t = sqr(B*B-4*C)
print((-B - t)//2)


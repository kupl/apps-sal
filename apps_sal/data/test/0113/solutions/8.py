def gsd(a, b):
    if b == 0:
        return a
    return gsd(b, a % b)


(n, k) = list(map(int, input().split()))
print(n * (10 ** k // gsd(n, 10 ** k)))

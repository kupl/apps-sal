def water(A, B, C):
    result = C - (A - B)
    return max(0, result)


A, B, C = list(map(int, input().split()))

print((water(A, B, C)))


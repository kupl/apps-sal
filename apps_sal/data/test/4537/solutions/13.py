def LI():
    return list(map(int, input().split()))


A, B = LI()
print((max(A + B, A - B, A * B)))

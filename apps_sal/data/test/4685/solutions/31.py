A, B, C = sorted([int(i) for i in input().split()])
K = int(input())
print((A + B + (C * (2**K))))

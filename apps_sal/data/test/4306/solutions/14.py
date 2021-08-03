A, B, C, D = [int(i) for i in input().split()]

t1 = max(A, C)
t2 = min(B, D)

print((max(0, t2 - t1)))

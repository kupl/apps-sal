a = [int(e) for e in input().split()]
a.sort()
A = a[-1] - a[0]
B = a[-1] - a[1]
C = a[-1] - a[2]
print(A, B, C)

N, M, K = map(int, input().split())
A = [int(a) for a in input().split()]
A = sorted(A)

m1 = A[-1]
m2 = A[-2]

a = M // (K + 1)
b = M % (K + 1)

print(a * (m1 * K + m2) + m1 * b)

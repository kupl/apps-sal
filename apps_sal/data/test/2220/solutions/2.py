(n, m, k) = list(map(int, input().split()))
A = sorted([int(x) for x in input().split()])
m1 = A[-1]
m2 = A[-2]
print(m // (k + 1) * (m1 * k + m2) + m % (k + 1) * m1)

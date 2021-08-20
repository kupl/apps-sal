(n, m, z) = list(map(int, input().split()))
print(len([i for i in range(1, z + 1) if i % n == 0 and i % m == 0]))

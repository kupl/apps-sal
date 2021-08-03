n, m = [int(x) for x in input().strip().split()]
print(''.join('01' for _ in range(n // 2 + 1))[:n])

n = int(input())
gates = [int(input()) for _ in range(5)]
bn = min(gates)

print((int((n + bn - 1) / bn) + 4))

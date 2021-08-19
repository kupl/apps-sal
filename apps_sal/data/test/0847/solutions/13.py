(n, x) = map(int, input().split())
print(str((abs(sum(map(int, input().split()))) + x - 1) // x))

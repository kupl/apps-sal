(a, b) = map(int, input().split())
print((f'{a}' * b, f'{b}' * a)[b <= a])

a, b, k = map(int, input().split())

aa = max (a - k, 0)
rest = max(k - a, 0)
bb = max (b - rest, 0)
print(f'{aa} {bb}')

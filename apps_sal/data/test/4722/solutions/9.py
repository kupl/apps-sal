(a, b) = list(map(int, input().split()))
print('Possible' if any([x % 3 == 0 for x in [a, b, a + b]]) else 'Impossible')

A, B, C, X, Y = map(int, input().split())

mini = float('inf')

for i in range(10**6 + 1):
    calc = i * 2 * C + max(0, X - i) * A + max(0, Y - i) * B
    if calc < mini:
        mini = calc

print(mini)

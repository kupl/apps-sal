(a, b, c, d) = map(int, input().split())
t_1 = (a + d - 1) // d
t_2 = (c + b - 1) // b
print('Yes' if t_2 <= t_1 else 'No')

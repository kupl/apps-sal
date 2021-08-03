a, b = input(), input()
n = [i + j for i, j in zip(a, b)]
print(*[n, n + [a[-1]]][len(a) - len(b) == 1], sep='')

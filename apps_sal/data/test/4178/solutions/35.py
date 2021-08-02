input(); a = [*map(int, input().split())]; b = sorted(a)
print('YNeos'[any(abs(i - j) > 1 for i, j in zip(a, b))::2])

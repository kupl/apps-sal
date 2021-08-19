n = int(input())
num = sorted([int(input()) for _ in range(n)])
print(sum([x * y for (x, y) in zip(num, reversed(num))]) % 10007)

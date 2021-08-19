(a, b) = list(map(int, input().split()))
n = b - a - 1
an = n * (n + 1) // 2
print(an - a)

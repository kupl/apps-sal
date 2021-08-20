(n, m) = list(map(int, input().split()))
a = sum((int(ai) % 2 for ai in input().split()))
b = sum((int(bi) % 2 for bi in input().split()))
print(min(a, m - b) + min(b, n - a))

n = int(input())
X = list(map(int, input().split()))
m1 = sum(X) // n
m2 = (sum(X) + (n - 1)) // n
a1 = sum([(x - m1) ** 2 for x in X])
a2 = sum([(x - m2) ** 2 for x in X])
print(min(a1, a2))

k, a, b, v = list(map(int, input().split()))
outcome = 0
while a > 0:
    outcome += 1
    kn = min(k, b+1)
    a -= kn * v
    b = max(0, b - kn + 1)
print(outcome)



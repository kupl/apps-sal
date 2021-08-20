(W, a, b) = list(map(int, input().split()))
print(0 if W > abs(a - b) else abs(a - b) - W)

(W, a, b) = map(int, input().split())
print([abs(a - b) - W, 0][abs(a - b) <= W])

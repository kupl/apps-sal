X, Y = list(map(int, input().split()))
ans = 'Brown' if abs(X - Y) <= 1 else 'Alice'
print(ans)

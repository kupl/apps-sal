n, m, x, y = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
if max(max(X), x) < min(min(Y), y):
    print("No War")
else:
    print("War")

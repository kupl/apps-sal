n, m, x, y = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
if max(X) < min(Y) and max(X) + 1 > x and max(X) + 1 <= y:
    print("No War")
else:
    print("War")

N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
for Z in range(X + 1, Y + 1):
    if max(x) < Z <= min(y):
        print("No War")
        return
print("War")

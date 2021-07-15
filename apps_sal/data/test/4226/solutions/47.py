X, Y = list(map(int, input().split()))

T = 0
K = 0

for i in range(X + 1):
    j = X - i

    if 2 * i + 4 * j == Y:
        print("Yes")
        return
print("No")


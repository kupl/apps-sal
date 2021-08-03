X, Y = list(map(int, input().split()))
K = 0

if Y % 2 == 0:
    K = Y // 2 - X
    if K >= 0:
        if X - K >= 0:
            print("Yes")
            return

print("No")

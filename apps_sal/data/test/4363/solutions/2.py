(K, S) = map(int, input().split())
kotae = 0
for Z in range(K + 1):
    X_plus_Y = S - Z
    for Y in range(K + 1):
        X = X_plus_Y - Y
        if 0 <= X <= K:
            kotae += 1
print(kotae)

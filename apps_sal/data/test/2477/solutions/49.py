
def fun(X_high, X_low, K, line):
    X = (X_high + X_low) // 2
    cnt = 0
    for tree in line:
        if tree <= X:
            continue
        else:
            q, r = divmod(tree, X)
            if r == 0:
                q -= 1
            cnt += q
    if cnt > K:
        X_low = X
    else:
        X_high = X
    return X_high, X_low


N, K = map(int, input().split(" "))
line = list(map(int, input().split(" ")))

X_high = max(line)
X_low = 0

while (X_high - X_low) > 1:
    X_high, X_low = fun(X_high, X_low, K, line)

print(X_high)

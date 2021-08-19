# 072_a
X, t = map(int, input().split())
if (1 <= X and X <= 10**9) and (1 <= t and t <= 10**9):
    if X <= t:
        print(0)
    else:
        print(X - t)

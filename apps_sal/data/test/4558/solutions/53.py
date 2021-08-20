(X, t) = map(int, input().split())
answer = X - t
if X <= t:
    print(0)
else:
    print(answer)

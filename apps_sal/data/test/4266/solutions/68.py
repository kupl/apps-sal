K, X = map(int, input().split())

if X - K + 1 < -1000000:
    ans = list(range(-100000, X + K))
elif X + K > 1000000:
    ans = list(range(X - K + 1, 1000000))
else:
    ans = list(range(X - K + 1, X + K))

ans = map(str, ans)
print(' '.join(ans))

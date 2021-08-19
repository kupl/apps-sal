(N, K) = map(int, input().split())
(*X,) = map(int, input().split())
i = 0
ans = []
while i + K - 1 < N:
    (a, b) = (X[i], X[i + K - 1])
    if b < 0:
        ans.append(abs(a))
    elif a > 0:
        ans.append(b)
    else:
        a = abs(a)
        ans.append(a + b + min(a, b))
    i += 1
print(min(ans))

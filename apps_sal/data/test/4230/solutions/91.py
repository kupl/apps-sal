(X, N) = list(map(int, input().split()))
p = list(map(int, input().split()))
ans = None
diff = 1000
if X not in p:
    ans = X
else:
    for i in range(-1, max(max(p), X) + 2):
        if i in p:
            continue
        if abs(X - i) < diff:
            diff = abs(X - i)
            ans = i
print(ans)

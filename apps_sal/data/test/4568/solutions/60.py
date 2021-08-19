n = int(input())
S = input()
ans = 0
for i in range(1, n):
    (X, Y) = (S[:i], S[i:])
    cnt = 0
    for x in set(X):
        if x in Y:
            cnt += 1
    ans = max(cnt, ans)
print(ans)

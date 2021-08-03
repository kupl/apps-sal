K, X = map(int, input().split())

ans = str(X - K + 1)
for i in range(X - K + 2, X + K):
    ans += " " + str(i)
print(ans)

(X, Y) = list(map(int, input().split()))
ans = 'No'
for a in range(X + 1):
    b = X - a
    if Y == 2 * a + 4 * b:
        ans = 'Yes'
        break
print(ans)

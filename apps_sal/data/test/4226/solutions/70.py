(X, Y) = map(int, input().split())
ans = 'No'
for i in range(0, X + 1):
    if i * 2 + (X - i) * 4 == Y:
        ans = 'Yes'
        break
print(ans)

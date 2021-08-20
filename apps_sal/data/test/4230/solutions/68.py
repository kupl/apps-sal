(X, N) = list(map(int, input().split()))
p = list(map(int, input().split()))
ans = 0
for i in range(1, 102):
    if i not in p:
        if abs(X - i) < abs(X - ans):
            ans = i
print(ans)

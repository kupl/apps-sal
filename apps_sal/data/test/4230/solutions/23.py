(X, N) = map(int, input().split())
p = list(map(int, input().split()))
mini = 100000
for i in range(X + 200):
    if i in p:
        continue
    if abs(i - X) < mini:
        mini = abs(i - X)
        ans = i
print(ans)

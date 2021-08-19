n = int(input())
ans = 10 ** 7 + 9
x = list(map(int, input().split()))
X = len(x)
for i in range(100):
    total = 0
    for j in range(X):
        total += (x[j] - i) ** 2
    else:
        ans = min(ans, total)
print(ans)

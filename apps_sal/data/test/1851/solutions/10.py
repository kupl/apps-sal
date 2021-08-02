num = input()
maxi = 0
X = list(map(int, input().split()))
ans = 0
for i in range(int(num)):
    maxi = max(X[i], maxi)
    if i + 1 == maxi:
        ans += 1
print(ans)

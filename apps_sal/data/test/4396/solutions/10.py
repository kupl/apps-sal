N = int(input())
X = []
U = []
for _ in range(N):
    x, u = input().split()
    X.append(float(x))
    U.append(u)

ans = 0
for x, u in zip(X, U):
    if u == 'JPY':
        ans += x
    else:
        ans += x*380000.
print(ans)


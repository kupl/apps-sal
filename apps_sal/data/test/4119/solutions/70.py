N, M = list(map(int, input().split()))
X = list(map(int, input().split()))
X.sort()

D = [r - l for l, r in zip(X, X[1:])]
D.sort()

ans = sum(D)
while D and N > 1:
    N -= 1
    ans -= D.pop()
print(ans)


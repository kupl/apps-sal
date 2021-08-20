(X, Y) = map(int, input().split())
ans = []
n = X
while n <= Y:
    ans.append(n)
    n *= 2
print(len(ans))

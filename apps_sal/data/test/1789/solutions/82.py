(A, B, X, Y) = map(int, input().split())
x = A * 2
y = B * 2 + 1
l = abs(y - x)
o = X
t = min(X * 2, Y)
ans = l // 2 * t + l % 2 * o
print(ans)

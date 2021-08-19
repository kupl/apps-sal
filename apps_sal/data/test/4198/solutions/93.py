(A, B, X) = map(int, input().split())
ans = 0
for i in range(1, 11):
    N = min(int(str(9) * i), (X - B * i) // A)
    ans = max(N, ans)
ans = min(10 ** 9, ans)
print(ans)

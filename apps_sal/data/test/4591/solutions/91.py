A, B, C, X, Y = map(int, input().split())

ans = max(A, B, C) * (X + Y)
for i in range(max(X, Y) * 2 + 1):
    price = i * C
    price += max(X - i // 2, 0) * A
    price += max(Y - i // 2, 0) * B
    ans = min(ans, price)
    # print(i, X-i//2, Y-i//2, price, ans)
print(ans)

X = int(input())
ans, rem = divmod(X, 500)
ans *= 1000
ans += rem // 5 * 5
print(ans)

N, X, T = map(int, input().split())
ans = 0
if N % X == 0:
    num = N // X
    ans += T * num
else:
    num = N // X + 1
    ans += T * num
print(ans)

(T, S, q) = map(int, input().split())
ans = 0
x = 0
while x < T:
    x = S * q
    S = x
    ans += 1
print(ans)

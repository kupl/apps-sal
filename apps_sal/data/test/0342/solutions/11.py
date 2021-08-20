(a, b, c) = list(map(int, input().split()))
ans = 2 * c
m = min(a, b)
a -= m
b -= m
ans += 2 * m
if a + b > 0:
    ans += 1
print(ans)

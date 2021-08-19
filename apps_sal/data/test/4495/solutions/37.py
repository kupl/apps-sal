(a, b, x) = list(map(int, input().split()))
ans = (b - a) // x
if (x - a % x) % x + b % x < x:
    ans += 1
print(ans)

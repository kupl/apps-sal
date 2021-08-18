(a, b, ab) = (int(x) for x in input().split())
m = min(a, b)
ans = ab * 2 + 2 * m

a -= m
b -= m

if a or b:
    ans += 1
print(ans)

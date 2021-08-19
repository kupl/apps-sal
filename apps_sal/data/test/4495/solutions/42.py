(a, b, x) = map(int, input().split())
ans = b // x - a // x + (a % x == 0)
print(ans)

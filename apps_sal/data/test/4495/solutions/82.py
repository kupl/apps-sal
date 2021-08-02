a, b, x = map(int, input().split())
ans = 0
n_a = a // x
n_b = b // x
if a % x == 0:
    ans += 1
ans += n_b - n_a
print(ans)

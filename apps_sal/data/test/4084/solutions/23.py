(n, a, b) = list(map(int, input().split()))
c = a + b
div = n // c
mod = n % c
if mod > a:
    mod = a
ans = div * a + mod
print(ans)

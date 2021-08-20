(n, a, x, b, y) = list(map(int, input().split()))
ans = 'NO'
if a == b:
    ans = 'YES'
while a != x and b != y:
    if a == n:
        a = 0
    a += 1
    if b == 1:
        b = n + 1
    b -= 1
    if a == b:
        ans = 'YES'
print(ans)

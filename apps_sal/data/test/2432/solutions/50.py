n = int(input())
me = [4, 1, 3, 2, 0, 5]
ans = 0
for _ in range(6):
    if n % 2 == 1:
        ans += 2 ** me[_]
    n //= 2
print(ans)

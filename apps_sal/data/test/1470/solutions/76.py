x = int(input())

m, r = divmod(x, 11)

if r == 0:
    ans = 2 * m
elif r <= 6:
    ans = 2 * m + 1
else:
    ans = 2 * (m + 1)

print(ans)

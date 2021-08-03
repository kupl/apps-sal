x = int(input())
d, m = divmod(x, 11)
ans = d * 2
if 0 < m <= 6:
    ans += 1
elif m >= 7:
    ans += 2
print(ans)

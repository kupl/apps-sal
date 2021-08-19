s = "0" + input()
ans = 0
n = len(s)
f = 0
p = 0
for i in range(1, n + 1):
    n = int(s[-i])
    # n += f
    if p + (n > 4) > 5:
        f = 1
    else:
        # ans += f
        f = 0
    n += f
    ans += min(n, 10 - n)
    p = n
# ans += f
print(ans)

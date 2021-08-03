x = int(input())
ans = (x // 11) * 2
y = x % 11
if y == 0:
    print(ans)
elif y <= 6:
    print((ans + 1))
else:
    print((ans + 2))

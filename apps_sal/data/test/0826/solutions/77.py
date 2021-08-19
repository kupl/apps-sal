n = int(input())
ans = n + 1
square = int((n * 2 + 2) ** 0.5)
if n * 2 + 2 - square ** 2 - square >= 0:
    pass
else:
    square -= 1
print(ans - square)

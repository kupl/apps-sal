a = int(input())
if a % 2 == 0:
    ans = int((a / 2) ** 2)
else:
    ans = int((a - 1) / 2 * ((a + 1) / 2))
print(ans)

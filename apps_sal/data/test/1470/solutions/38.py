x = int(input())
a = x // 11
b = x % 11
if b == 0:
    ans = a * 2
elif b in range(1, 7):
    ans = a * 2 + 1
else:
    ans = a * 2 + 2
print(ans)

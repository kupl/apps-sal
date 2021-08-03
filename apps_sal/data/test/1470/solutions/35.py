x = int(input())

c = (x // 11) * 2
if x % 11 == 0:
    ans = c
elif x % 11 <= 6:
    ans = c + 1
else:
    ans = c + 2

print(ans)

x = int(input())
t = x // 11
if x % 11 == 0:
    print((t * 2))
elif x % 11 <= 6:
    print((t * 2 + 1))
else:
    print((t * 2 + 2))

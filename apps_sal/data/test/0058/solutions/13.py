n = int(input())
a = int(input())
b = int(input())
ans = 1
rem = n
sides = 6
if (a + a + b) * 2 <= n:
    print(1)
elif a * 2 + b <= n or (a * 4 <= n and b * 2 <= n):
    print(2)
elif a * 4 <= n and b <= n or (b * 2 <= n and a * 2 <= n) or (a + b <= n and a * 2 <= n):
    print(3)
elif a * 2 <= n and b <= n or (a + b <= n and a <= n):
    print(4)
elif b * 2 <= n and a <= n:
    print(5)
else:
    print(6)

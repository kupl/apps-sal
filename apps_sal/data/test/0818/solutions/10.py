n = int(input())
if n == 1 or n == 2:
    print(-1)
elif n == 3:
    print(210)
else:
    a = (10**(n - 1))
    if a % 210 == 0:
        print(a)
    else:
        print(((a // 210) + 1) * 210)

n = int(input())

f = False

x = sum(list(map(int, str(n))))

if n % x == 0:
    f = True

if f:
    print("Yes")
else:
    print("No")

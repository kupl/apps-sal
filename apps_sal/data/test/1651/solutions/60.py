s, p = map(int, input().split())
x = 1
while x**2 <= p:
    if p % x == 0:
        y = p // x
        if x + y == s:
            print("Yes")
            return
    x += 1
print("No")

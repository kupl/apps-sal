(a, b) = map(int, input().split())
t = 0
while a > 0 and b > 0:
    if a > b or (b == 1 and a != 1):
        b += 1
        a -= 2
    elif b > a or (a == 1 and b != 1):
        b -= 2
        a += 1
    elif a == b and a != 1:
        b += 1
        a -= 2
    else:
        break
    t += 1
print(t)

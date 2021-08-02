
my_str = input().split()
a, b = int(my_str[0]), int(my_str[1])
c = 0
while a > b and b > 0:
    t = a
    a = b
    c += int(t / b)
    b = t % b
    if b > a:
        t = a
        a = b
        b = t
print(c)

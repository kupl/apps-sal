n = int(input())


def sum(n):
    t = 0
    while n != 0:
        t = t + n % 10
        n = n // 10
    return t


i = 0
j = n
while j != 0:
    t = sum(i)
    if t <= 10 and t != 0:
        j = j - 1
    if j == 0:
        print(str(i) + str(10 - t))
    i = i + 1

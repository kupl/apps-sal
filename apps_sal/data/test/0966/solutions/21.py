year = int(input())

for i in range(year + 1, 10000):
    y = i
    a = y // 1000
    y = y - a * 1000
    b = y // 100
    y = y - b * 100
    c = y // 10
    y = y - c * 10
    lst = [a, b, c, y]
    lst.sort()
    if lst[0] != lst[1] and lst[1] != lst[2] and lst[2] != lst[3]:
        print(i)
        break

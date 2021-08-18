X = int(input())

value = 100
year = 1

while True:
    value = value + value // 100
    if value >= X:
        print(year)
        break
    else:
        year = year + 1

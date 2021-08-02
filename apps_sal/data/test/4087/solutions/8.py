n = int(input())
while 1:
    y = str(n)
    counter = 0
    for item in y:
        counter += int(item)
    if counter % 4 == 0:
        print(y)
        break
    n += 1

x = int(input())
place = 0
i = 1
while 1:
    if place + i >= x:
        print(i)
        break
    else:
        place += i
        i += 1

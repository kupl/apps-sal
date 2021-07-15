day = 0
y = int(input())
leap = y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

y += 1
days = 366%7 if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0) else 365%7
day = (day + days)%7

while True:
    if day == 0:
        this_leap = y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)
        if leap == this_leap:
            break
        
    y += 1
    days = 366%7 if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0) else 365%7
    day = (day + days)%7

print(y)

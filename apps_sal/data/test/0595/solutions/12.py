#B
y=int(input())

def visok_y(y):
    if ((y%4==0) and (y%100!=0)) or (y%400==0):
        return 2
    else:
        return 1
y_v=visok_y(y)
day=0

while True:
    day=(day+visok_y(y))%7
    y+=1
    if day==0 and visok_y(y)==y_v:
        print(y)
        break


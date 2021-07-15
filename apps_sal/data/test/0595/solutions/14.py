def leap(y):
    return y % 400 == 0 or y % 4 == 0 and y % 100 != 0

sun,mon,tue,wed,thu,fri,sat = [i for i in range(7)]
l = {i:0 for i in range(1000,110000)}
l[2016] = fri
for i in range(2015, 999, -1):
    if leap(i):
        l[i] = (7+l[i+1]-2)%7
    else:
        l[i] = (7+l[i+1]-1)%7

for i in range(2017, 110000):
    if leap(i-1):
        l[i] = (l[i-1] + 2)%7
    else:
        l[i] = (l[i-1] + 1)%7

year = int(input())
for i in range(year+1, 110000):
    if l[i] == l[year] and leap(i) == leap(year):
        print(i)
        break


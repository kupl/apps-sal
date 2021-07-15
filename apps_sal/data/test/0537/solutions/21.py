import math

students, ratio = input().split()
students, ratio = int(students), int(ratio)

dip = math.floor((students/2)/(ratio+1))
win = dip * ratio
print(dip, win, students - dip - win)

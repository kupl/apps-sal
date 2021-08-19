y = int(input())
y = y + 1


def isDistinct(year):
    sy = str(year)
    li = []
    for i in sy:
        if i in li:
            return False
        li.append(i)
    return True


while not isDistinct(y):
    y = y + 1
print(y)

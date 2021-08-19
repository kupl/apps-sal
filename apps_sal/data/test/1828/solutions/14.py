num = int(input())
track = []
for i in range(num + 1):
    temp = list(map(int, input().split()))
    track.append(temp)


def checkDirection(pointOne, pointTwo):
    if pointOne[0] < pointTwo[0]:
        return 'E'
    if pointOne[0] > pointTwo[0]:
        return 'W'
    if pointOne[1] < pointTwo[1]:
        return 'N'
    if pointOne[1] > pointTwo[1]:
        return 'S'


def checkDanger(pointOne, pointTwo, pointThree):
    first = checkDirection(pointOne, pointTwo)
    second = checkDirection(pointTwo, pointThree)
    if first == 'W' and second == 'S' or (first == 'S' and second == 'E') or (first == 'N' and second == 'W') or (first == 'E' and second == 'N'):
        return True
    else:
        return False


numDanger = 0
for i in range(1, len(track) - 1):
    if checkDanger(track[i - 1], track[i], track[i + 1]):
        numDanger += 1
print(numDanger)

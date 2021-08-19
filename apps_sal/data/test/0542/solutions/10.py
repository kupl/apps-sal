points = int(input())

firstpoints = []
secondpoints = []
ans = "k"
for s in range(points):
    point = int(input())
    if point > 0:
        firstpoints.append(int(point))
    elif point < 0:
        secondpoints.append(int(point))
    if s == points - 1 and point > 0:
        ans = "l"  # first player last punch

if sum(firstpoints) == abs(sum(secondpoints)):
    for i in range(max(len(firstpoints), len(secondpoints))):
        if firstpoints[i] > abs(secondpoints[i]):
            print("first")
            break
        elif firstpoints[i] < abs(secondpoints[i]):
            print("second")
            break
        elif i == min(len(firstpoints), len(secondpoints)) - 1:
            if ans == "l":
                print("first")
                break
            else:
                print("second")
                break


elif sum(firstpoints) > abs(sum(secondpoints)):
    print("first")
else:
    print("second")

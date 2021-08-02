def check_polygon(angle):
    no_sides = -360 / (angle - 180)
    if no_sides - int(no_sides) == 0:
        return True
    else:
        return False


testcases = []
no_testcases = int(input())
for i in range(no_testcases):
    testcases.append(int(input()))

for testcase in testcases:
    if check_polygon(testcase):
        print("YES")
    else:
        print("NO")

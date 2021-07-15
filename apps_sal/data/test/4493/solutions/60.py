#18
import sys
c = [list(map(int,input().split())) for i in range(3)]

if not(c[0][0] - c[0][1] == c[1][0] - c[1][1] == c[2][0] - c[2][1]):
    print("No")
    return
if not(c[0][0] - c[0][2] == c[1][0] - c[1][2] == c[2][0] - c[2][2]):
    print("No")
    return
if not(c[0][1] - c[0][2] == c[1][1] - c[1][2] == c[2][1] - c[2][2]):
    print("No")
    return
if not(c[0][0] - c[1][0] == c[0][1] - c[1][1] == c[0][2] - c[1][2]):
    print("No")
    return
if not(c[0][0] - c[2][0] == c[0][1] - c[2][1] == c[0][2] - c[2][2]):
    print("No")
    return
if not(c[1][0] - c[2][0] == c[1][1] - c[2][1] == c[1][2] - c[2][2]):
    print("No")
    return
print("Yes")
    



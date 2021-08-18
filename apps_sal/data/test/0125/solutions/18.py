
a = input().split()
b = input().split()
c = input().split()
d = input().split()

lights = [a, b, c, d]

for i in range(0, 4):
    if int(lights[i][3]) == 1:
        if int(lights[i][0]) == 1 or int(lights[i][1]) == 1 or int(lights[i][2]) == 1:
            print("YES")
            break
        if i == 0:
            if int(lights[1][0]) == 1 or int(lights[2][1]) == 1 or int(lights[3][2]) == 1:
                print("YES")
                break
        if i == 1:
            if int(lights[2][0]) == 1 or int(lights[3][1]) == 1 or int(lights[0][2]) == 1:
                print("YES")
                break
        if i == 2:
            if int(lights[3][0]) == 1 or int(lights[0][1]) == 1 or int(lights[1][2]) == 1:
                print("YES")
                break
        if i == 3:
            if int(lights[0][0]) == 1 or int(lights[1][1]) == 1 or int(lights[2][2]) == 1:
                print("YES")
                break
    if i == 3:
        print("NO")

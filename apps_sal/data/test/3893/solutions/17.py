a, b = list(map(int, input("").split(" ")))
c, d = list(map(int, input("").split(" ")))
dumb = int(input(""))
lines = []
for value in range(dumb):
    lines.append(input("").split(" "))
count = 0
check1 = 0
check2 = 0
for value in lines:
    if (int(value[0]) * a + int(value[1]) * b + int(value[2]) >= 0):
        check1 = 1
    else:
        check1 = -1
    if(int(value[0]) * c + int(value[1]) * d + int(value[2]) >= 0):
        check2 = 1
    else:
        check2 = -1
    if check2 != check1:
        count = count + 1
print(count)

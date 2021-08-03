N = input()
Dies = []

for x in range(int(N)):
    Dies.append(input().split())

counter = 0
z = 0
for y in Dies:
    if y[0] == y[1]:
        counter = counter + 1

    else:
        counter = 0

    if counter == 3:
        z = 1
        break

if z == 0:
    print("No")

else:
    print("Yes")

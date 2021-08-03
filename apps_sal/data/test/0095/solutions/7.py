n = input()
n = [int(I) for I in input().split(" ")]

up = False
down = False
constant = False

for I in range(1, len(n)):
    if n[I] == n[I - 1]:  # CONSTANT
        if down == True:
            print("NO")
            return
        else:
            constant = True
    elif n[I] > n[I - 1]:  # UP
        if (constant or down) == True:
            print("NO")
            return
        else:
            up = True
    else:
        down = True
print("YES")

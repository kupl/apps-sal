x = list(input())

a1 = (x[0] == x[2]) and (x[1] == x[3])
a2 = (x[0] == x[1]) and (x[2] == x[3])
a3 = (x[0] == x[3]) and (x[1] == x[2])
b = len(set(x)) == 2

if b and (a1 or a2 or a3):
    print("Yes")
else:
    print("No")

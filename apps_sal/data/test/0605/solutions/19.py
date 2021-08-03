p = input().split()
a = int(p[0])
b = int(p[1])
c = int(p[2])
d = int(p[3])
x = max((3 * a) // 10, a - (a // 250) * c)
y = max((3 * b) // 10, b - (b // 250) * d)
if(x > y):
    print("Misha")
elif(y > x):
    print("Vasya")
else:
    print("Tie")

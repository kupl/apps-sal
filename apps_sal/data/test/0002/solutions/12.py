a = int(input())
b = a
nr = 1
while b > 9:
    nr *= 10
    b /= 10
print(int(b + 1) * int(nr) - int(a))

x = int(input())
a = int(input())
b = int(input())
x -= a

while(1):
    x -= b
    if x - b < 0:
        print(x)
        break

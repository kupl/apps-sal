a = int(input())
b = int(input())
x = 1
for i in range(a):
    if x + b > x * 2:
        x = x * 2
    else:
        x = x + b
print(x)

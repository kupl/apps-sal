from math import sqrt
input()
a = list(map(int, input().split()))
max = -1000000
for i in a:
    if i >= 0:
        if not sqrt(i).is_integer():
            if i > max:
                max = i
    elif(i > max):
        max = i
print(max)

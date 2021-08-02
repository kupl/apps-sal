import math

list = input().split()

num = int(list[0] + list[1])

num_squrt = math.sqrt(num)

if num_squrt.is_integer() == True:
    print("Yes")
else:
    print("No")

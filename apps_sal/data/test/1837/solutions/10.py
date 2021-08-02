# FixedPoints

numbers = int(input())
array = input().split(" ")
array = [int(x) for x in array]

points = 0
one = False
two = False
for i in range(numbers):
    if array[i] == i:
        points += 1
    else:
        j = array[i]
        if two == False:
            if array[i] == j and array[j] == i:
                two = True
        if one == False:
            if array[i] == j or array[j] == i:
                one = True
if two == True:
    points += 2
elif one == True:
    points += 1
print(points)

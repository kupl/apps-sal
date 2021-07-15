rStr = input()

A = int(rStr.split(' ')[0])
B = int(rStr.split(' ')[1])

result = 0
index = 0

while index < 2 :
    if A <= B :
        result += B
        B = B - 1
    else :
        result += A
        A = A - 1
    index = index + 1

print(result)

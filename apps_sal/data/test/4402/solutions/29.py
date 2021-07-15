rStr = input()

A = int(rStr.split(' ')[0])
B = int(rStr.split(' ')[1])

result = 0

if 13 <= A :
    result = B

elif A <= 5 :
    result = 0

else :
    result = int(B / 2)

print(result)

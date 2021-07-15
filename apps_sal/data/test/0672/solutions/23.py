x = input("").split(" ")
a = int(x[0])
b = int(x[1])
list = []
answer = 0
if a == b:
    print("infinity")
else:
    value = 1
    while value**2 <= a-b:
        if (a-b)%value == 0:
            list.append(value)
            if (value != (a-b)/value):
                list.append((a-b)/value)
        value = value + 1
    for value in list:
        if value > b:
            answer = answer + 1
    
    print(answer)

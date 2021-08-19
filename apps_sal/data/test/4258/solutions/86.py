rStr = input()
A = int(rStr.split(' ')[0])
B = int(rStr.split(' ')[1])
T = int(rStr.split(' ')[2])
result = int((T + 0.5) / A) * B
print(result)

import math

n = int(input())
string = input()

arr = [0] * 10
for i in range(len(string)):
    if(string[i] == 'L'):
        index = 0
        while(arr[index] != 0):
            index += 1
        arr[index] = 1
    elif(string[i] == 'R'):
        index = 9
        while(arr[index] != 0):
            index -= 1
        arr[index] = 1
    else:
        arr[int(string[i])] = 0

printstring = ""
for i in range(10):
    printstring += str(arr[i])
print(printstring)

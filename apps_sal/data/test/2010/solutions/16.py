firstLine = list(map(int, input().split()))
array = list(map(int, input().split()))

arraySize = firstLine[0]
numOperations = firstLine[1]
totalSum = 0
s = ""

for i in range(numOperations):
    command = list(map(int, input().split()))
    op = command[0]
    param1 = command[1]

    if(op == 1):
      array[param1 - 1] = command[2] - totalSum
    elif(op == 2):
      totalSum += param1
    else:
      s += str(array[param1 - 1] + totalSum) + '\n'

print(s)


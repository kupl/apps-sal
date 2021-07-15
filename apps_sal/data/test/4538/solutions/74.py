import sys
import math

index = 0
count = 0
for input in sys.stdin:
    formattedInput = input.replace("\n", "").split(" ")
    if index == 0:
        N = int(formattedInput[0])
        D = int(formattedInput[1])
        index += 1
        continue
    root = math.sqrt(int(formattedInput[0]) ** 2 + int(formattedInput[1]) ** 2)
    if D >= root:
        count += 1
    index += 1

print(count)


from sys import stdin
from math import *

line = stdin.readline().rstrip().split()
n = int(line[0])

numbers = stdin.readline().rstrip().split()[0]
numbers2 = stdin.readline().rstrip().split()[0]

moves = 0
for i in range(int(ceil(len(numbers)/2))):
    if i == int(ceil(len(numbers)/2))-1 and len(numbers)%2 == 1:
        if numbers[i] != numbers2[i]:
            moves+=1
        break
    else:
        if numbers2[i] == numbers2[n-(i+1)]:
            if numbers[i] != numbers[n - (i + 1)]:
                moves+=1
        else:
            if numbers[i] == numbers2[i] and  numbers[n-(i+1)] == numbers2[n-(i+1)]:
                moves +=0
            elif numbers[i] == numbers2[n-(i+1)] and  numbers[n-(i+1)] == numbers2[i]:
                moves+=0
            elif numbers[i] == numbers2[i] or numbers[i] == numbers2[n-(i+1)] or numbers[n-(i+1)] == numbers2[i] or numbers[n-(i+1)] == numbers2[n-(i+1)]:
                moves+=1
            else:
                moves+=2
print(moves)

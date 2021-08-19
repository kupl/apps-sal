from collections import deque
import sys
n = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().strip().split(' ')))
zeros = [-float('Inf')]
for i in range(n):
    if array[i] == 0:
        zeros.append(i)
zeros.append(float('Inf'))
j = 1
for i in range(n):
    if array[i] == 0:
        j += 1
        print(array[i], end=' ')
    else:
        aux = min(abs(zeros[j] - i), abs(zeros[j - 1] - i))
        print(aux, end=' ')

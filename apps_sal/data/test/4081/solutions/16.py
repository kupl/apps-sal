import sys
from collections import deque


fin = sys.stdin.readline
n = int(fin())
a_list = deque(int(elem) for elem in fin().split())
last_elem = float('-inf')
length_sequence = 0
operations = []
while a_list:
    if last_elem < a_list[-1] <= a_list[0]:
        last_elem = a_list.pop()
        operations.append("R")
    elif last_elem < a_list[0] <= a_list[-1]:
        last_elem = a_list.popleft()
        operations.append("L")
    elif a_list[0] < last_elem < a_list[-1]:
        last_elem = a_list.pop()
        operations.append("R")
    elif a_list[-1] < last_elem < a_list[0]:
        last_elem = a_list.popleft()
        operations.append("L")
    else:
        break
    length_sequence += 1
print(length_sequence)
print("".join(operations))


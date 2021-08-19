from collections import deque
n = int(input())
numbers = deque()
aux = list(map(int, input().split()))
for i in range(n):
    numbers.append(aux[i])
(ser, dim) = (0, 0)
for i in range(n):
    if numbers[0] > numbers[-1]:
        if i % 2 == 0:
            ser += numbers[0]
        else:
            dim += numbers[0]
        numbers.popleft()
    else:
        if i % 2 == 0:
            ser += numbers[-1]
        else:
            dim += numbers[-1]
        numbers.pop()
print(ser, dim)

n = int(input())
array = list(map(int, input().split()))
total = 0
minus = 0
zero = 0

for i in range(len(array)):
    if array[i] > 0:
        total += array[i] - 1
    elif array[i] < 0:
        minus += 1
        total += -1 - array[i]
    else:
        zero += 1
        total += 1

if minus % 2 and zero == 0:
    total += 2

print(total)

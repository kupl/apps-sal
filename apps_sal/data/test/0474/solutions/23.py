amount = int(input())
array = [int(s) for s in input().split()]
max_ = max(array)
counter = 0
counter_max = 0
for i in range(len(array)):
    if array[i] == max_:
        counter += 1
        if counter > counter_max:
            counter_max = counter
    else:
        counter = 0
print(counter_max)

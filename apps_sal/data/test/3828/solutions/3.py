n = int(input())
cars = [int(x) for x in input().split()]
sorted_cars = sorted(enumerate(cars), key = lambda x : x[1])
max_sorted_length = 1
length = 1
for i in range(1, n):
    if sorted_cars[i][0] > sorted_cars[i-1][0]:
        length += 1
    else:
        if max_sorted_length < length:
            max_sorted_length = length
        length = 1
if max_sorted_length < length: max_sorted_length = length
print(n - max_sorted_length)


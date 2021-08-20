(numbers, types) = list(map(int, input().split()))
position = [0] * numbers
binary_search_array = [1] * numbers
for i in range(numbers):
    position[i] = int(input().split()[0])
max_length = int(0)
for i in range(numbers):
    low = int(0)
    high = int(max_length)
    while low < high:
        mid = int((low + high) / 2)
        if binary_search_array[mid] <= position[i]:
            low = mid + 1
        else:
            high = mid
    binary_search_array[low] = position[i]
    if low == max_length:
        max_length += 1
print(numbers - max_length)

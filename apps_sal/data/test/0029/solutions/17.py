s = input()
arr = [int(i) for i in s]
count = 0
while count < 4:
    a = arr[0] + arr[1] + arr[2]
    b = arr[3] + arr[4] + arr[5]
    r = abs(a - b)
    if a == b:
        print(count)
        return
    if a < b:
        num_min = arr.index(min(arr[0], arr[1], arr[2]))
        num_max = arr.index(max(arr[3], arr[4], arr[5]))
    else:
        num_min = arr.index(min(arr[3], arr[4], arr[5]))
        num_max = arr.index(max(arr[0], arr[1], arr[2]))

    if r <= arr[num_max]:
        print(count + 1)
        return
    if r <= 9 - arr[num_min]:
        print(count + 1)
        return
    if 9 - arr[num_min] > arr[num_max]:
        arr[num_min] = 9
    else:
        arr[num_max] = 0
    count += 1
print(count)


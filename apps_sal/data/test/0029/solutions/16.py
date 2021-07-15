def change_num(left_arr, right_arr, count):
    min_n, max_n = 10, -1
        
    if sum(left_arr) > sum(right_arr):
        max_arr = left_arr
        min_arr = right_arr
    else:
        max_arr = right_arr
        min_arr = left_arr
        
    diff = sum(max_arr) - sum(min_arr)
    
    for i in range (3):
        if min_n > min_arr[i]:
            min_n = min_arr[i]
            min_i = i
        if max_n < max_arr[i]:
            max_n = max_arr[i]
            max_i = i
    if diff <= 9-min_n:
        count += 1
        return count
    elif diff <= max_n:
        count += 1
        return count
    elif max_n >= 9-min_n:
        max_arr[max_i] = 0
    else:
        min_arr[min_i] = 9
    count += 1
    return change_num(min_arr, max_arr, count)

msg = input() 

left = msg[:3]
right = msg[3:]

left_arr = []
right_arr = []

for char in left:
    left_arr.append(int(char))
for char in right:
    right_arr.append(int(char))

if sum(left_arr) == sum(right_arr):
    print(0)
else:
    print(change_num(left_arr, right_arr, 0))



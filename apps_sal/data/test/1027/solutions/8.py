arr = [int(x) for x in input().split()]
max_score = 0
for i in range(len(arr)):
    if arr[i] == 0:
        continue
    arr_copy = arr[:]
    arr_copy[i] = 0
    all_add = arr[i] // 14
    for j in range(14):
        arr_copy[j] += all_add
    for j in range(arr[i] - all_add * 14):
        arr_copy[(i + j + 1) % 14] += 1
    score = 0
    for j in arr_copy:
        if j > 0 and j % 2 == 0:
            score += j
    max_score = max(max_score, score)
print(max_score)


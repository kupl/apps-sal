n, k = input().split(' ')
n = int(n)
k = int(k)
arr = input().split(' ')
arr = list(map(lambda x: int(x), arr))

arr_d = [0] * 100005
arr_d_right = [0] * 100005


def count(i, k, n):
    # total_count = 0
    # while True:
    if i - k > 0:
        left_ind = i - k
    else:
        left_ind = 0

    if i + k < n - 1:
        right_ind = i + k
    else:
        right_ind = n - 1

    # print(arr_d[:n])
    # print(arr_d_right[:n])
    # print('>>>>>')
    next_i = arr[i] - 1

    if next_i != -1:
        prev_val = arr_d[next_i]
        #print(left_ind, right_ind)
        if left_ind <= arr_d_right[next_i]:
            left_ind = arr_d_right[next_i] + 1
    else:
        prev_val = 0

    arr_d[i] = prev_val + right_ind - left_ind + 1
    arr_d_right[i] = right_ind
    return arr_d[i]


res_arr = []
for ind in range(0, len(arr)):
    res_arr.append(str(count(ind, k, n)))

print(' '.join(res_arr))

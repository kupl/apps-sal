
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

INF = -100


def max_ind(array):
    return array.index(max(array))


answer_str_arr = []


def dfs(first_index):
    num_we_can_send = arr[first_index]
    arr[first_index] = INF

    for i in range(0, num_we_can_send):
        curr_max_ind = max_ind(arr)

        if arr[curr_max_ind] == INF:
            break

        answer_str_arr.append(str(first_index + 1) + ' ' + str(curr_max_ind + 1))

        dfs(curr_max_ind)


dfs(0)

is_huis = False
for el in arr:
    if el > INF:
        is_huis = True
        break

if is_huis:
    print('-1')
else:
    print(len(answer_str_arr))
    for answer in answer_str_arr:
        print(answer)

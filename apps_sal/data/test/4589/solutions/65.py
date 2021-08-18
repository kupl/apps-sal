import numpy as np


def get_num_bomb(arr, i, j):
    """
    docstring
    """
    temp_arr = np.full([arr.shape[0] + 2, arr.shape[1] + 2], False)
    temp_arr[1:1 + arr.shape[0], 1:1 + arr.shape[1]] = arr[:, :]
    slice = temp_arr[i:i + 3, j:j + 3]
    return slice.sum()


h, w = tuple([int(x) for x in input().split(" ")])
arr = []
ret_arr = [[0] * w for i in range(h)]
for i in range(h):
    x = list([(False if x == "." else True) for x in input()])
    arr.append(x)
arr = np.array(arr)
for i in range(h):
    for j in range(w):
        if arr[i, j] == True:
            ret_arr[i][j] = "
        else:
            ret_arr[i][j] = get_num_bomb(arr, i, j)
for lis in ret_arr:
    print(("".join(list([str(x) for x in lis]))))

import numpy as np


def get_num_bomb(arr, i, j):
    """
    docstring
    """
    temp_arr = np.full([arr.shape[0] + 2, arr.shape[1] + 2], False)
    temp_arr[1:1 + arr.shape[0], 1:1 + arr.shape[1]] = arr[:, :]
    return temp_arr[i + 1, j] + temp_arr[i, j + 1] + temp_arr[
        i + 2, j + 1] + temp_arr[i + 1, j + 2]


def main():
    h, w = tuple([int(x) for x in input().split(" ")])
    arr = []
    ret_arr = [[0] * w for i in range(h)]
    for i in range(h):
        x = list([(0 if x == "." else 1) for x in input()])
        arr.append(x)
    arr = np.array(arr)
    for i in range(h):
        for j in range(w):
            if arr[i, j] == 1:
                if get_num_bomb(arr, i, j) == 0:
                    return "No"
    return "Yes"


print((main()))

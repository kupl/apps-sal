import numpy as np


def main():
    (n, k) = list(map(int, input().split()))
    warps = list(map(int, input().split()))
    warps = [0] + warps
    warps = np.array(warps, dtype=int)
    order_num = np.zeros(len(warps) + 1, dtype=int)
    path_history = []
    node = 1
    while order_num[node] == 0:
        path_history.append(node)
        order_num[node] = len(path_history)
        node = warps[node]
    begin = order_num[node]
    if k <= begin:
        print(path_history[k])
    else:
        leng = len(path_history) - order_num[node] + 1
        index = (k - (begin - 1)) % leng
        print(path_history[begin - 1 + index])


main()

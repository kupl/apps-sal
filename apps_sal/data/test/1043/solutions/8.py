from math import log2, floor


def is_power2(num):
    return num != 0 and num & num - 1 == 0


def next_two_pow(val):
    pw = 0
    while 2 ** pw <= val:
        pw = +1
    return pw


n = int(input())
arr = [int(x) for x in input().split()]
win_idx = -1
selected = []
for i in range(1, n + 1):
    val = arr[i - 1]
    if win_idx == -1:
        if val == -1:
            win_idx = i
    elif is_power2(i):
        selected.append(val)
        selected.sort()
    elif len(selected) > 0 and val < selected[-1]:
        selected.pop()
        selected.append(val)
        selected.sort()
print(sum(selected))

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(val) for val in input().split(' ')]
    arr_idx = [idx for idx, val in enumerate(arr) if val]
    c = 0
    for i in range(len(arr_idx) - 1):
        c += arr_idx[i + 1] - arr_idx[i] - 1
    print(c)

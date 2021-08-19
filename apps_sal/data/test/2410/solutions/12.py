def max_subarray(arr):
    max_ending = max_current = arr[0]
    for i in arr[1:]:
        max_ending = max(i, max_ending + i)
        max_current = max(max_current, max_ending)
    return max_current


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    yas = sum(arr)
    adel = max(max_subarray(arr[1:]), max_subarray(arr[:n - 1]))
    if yas > adel:
        print('YES')
    else:
        print('NO')

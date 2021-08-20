for _ in range(int(input())):
    n = int(input())
    (*arr,) = list(map(int, input().split()))
    (*locks,) = list(map(int, input().split()))
    locked = []
    unlocked = []
    for (v, is_locked) in zip(arr, locks):
        if not is_locked:
            unlocked.append(v)
    unlocked.sort(reverse=True)
    arr_idx = 0
    unlocked_idx = 0
    while unlocked_idx < len(unlocked) and arr_idx < len(arr):
        if not locks[arr_idx]:
            arr[arr_idx] = unlocked[unlocked_idx]
            unlocked_idx += 1
        arr_idx += 1
    print(*arr)

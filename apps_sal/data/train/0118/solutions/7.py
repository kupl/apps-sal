def solve(n, x, arr):
    arr = sorted(arr)
    res = 0
    temp_length_so_far = 0
    for i in range(n - 1, -1, -1):
        temp_length_so_far += 1
        if arr[i] * temp_length_so_far >= x:
            res += 1
            temp_length_so_far = 0
    return res


T = int(input())
for _ in range(T):
    n, x = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(solve(n, x, arr))


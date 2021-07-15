def min_possible(arr):
    x = max(arr)
    return max(0, x - 25)


n = int(input().strip())
arr = list(map(int, input().strip().split()))
print(min_possible(arr))


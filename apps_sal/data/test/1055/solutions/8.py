def cek(arr):
    if arr == sorted(arr):
        return len(arr)
    else:
        return max(cek(arr[:len(arr) // 2]), cek(arr[len(arr) // 2:]))


n = int(input())
seq = list(map(int, input().split()))
print(cek(seq))

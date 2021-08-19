(n, k) = list(map(int, input().split()))
if k > n:
    k = n
arr = list(map(int, input().split()))
c = 0
cur = -1
while c < k:
    if arr[0] > arr[1]:
        if cur == arr[0]:
            c += 1
        else:
            cur = arr[0]
            c = 1
        arr = [arr[0]] + arr[2:] + [arr[1]]
    else:
        if cur == arr[1]:
            c += 1
        else:
            cur = arr[1]
            c = 1
        arr = arr[1:] + [arr[0]]
print(cur)

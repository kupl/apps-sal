n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()
n //= 2
arr = arr[n:]
n += 1
med = arr[0]
flag = 1
while flag < n:
    if arr[flag] > med:
        kk = (arr[flag] - med) * flag
        if kk < k:
            k -= kk
            med = arr[flag]
        else:
            med += k // flag
            k = 0
            break
    flag += 1
if flag == n:
    med += k // flag
print(med)

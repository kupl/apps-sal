n = int(input())
arr = list(map(int, input().split()))
arr.sort()
(i, j) = (0, 1)
ans = 'NO'
while j < n - 1:
    sm = arr[i] + arr[j]
    if sm > arr[j + 1]:
        ans = 'YES'
        break
    else:
        i += 1
        j += 1
print(ans)

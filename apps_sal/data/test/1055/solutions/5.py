n = int(input())
arr = list(map(int, input().split()))
ans = 1
size = 2
while size <= n:
    i = 0
    while i < n:
        j = i
        flag = 0
        while j < i + size - 1:
            if arr[j] <= arr[j + 1]:
                j += 1
            else:
                flag = 1
                break
        if flag == 0:
            ans = max(ans, size)
        i += size
    size = size * 2
print(ans)

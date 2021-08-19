n = int(input())
arr = list(map(int, input().split()))
const = arr[n - 1]
ans = n
for i in range(n - 2, 0, -1):
    if arr[i] != const:
        ans = i + 2
        break
    else:
        ans = i
print(ans)

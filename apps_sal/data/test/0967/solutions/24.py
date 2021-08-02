n = int(input())
arr = list(map(int, input().split()))
ans = n - 1
for i in range(-1, -n, -1):
    if arr[i] > arr[i - 1]:
        ans -= 1
    else:
        break
print(ans)

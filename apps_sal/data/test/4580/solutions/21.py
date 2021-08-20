n = int(input())
a = list(map(int, input().split()))
arr = [0] * 9
ans = [0] * 2
for i in a:
    if i // 400 < 8:
        arr[i // 400] = 1
    else:
        arr[8] += 1
left = sum(arr[:8])
right = arr[8]
ans[0] = left
if left == 0:
    ans[0] = 1
ans[1] = left + right
print(*ans)

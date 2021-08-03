n = int(input())
arr = list(map(int, input().split()))

ans = []

for (i, ele) in enumerate(arr):
    if i == 0:
        ans.append(ele)
    else:
        ans.append(min(arr[i - 1], arr[i]))
    if i == len(arr) - 1:
        ans.append(arr[-1])
print((sum(ans)))

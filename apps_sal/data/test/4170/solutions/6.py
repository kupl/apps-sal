n = int(input())
arr = list(map(int, input().split()))

cnt = 0
tmp = 0

for i in range(len(arr) - 1):
    if arr[i] >= arr[i + 1]:
        tmp += 1
    else:
        tmp = 0
    cnt = max(cnt, tmp)

print(cnt)

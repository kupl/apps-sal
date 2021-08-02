n = int(input())
mx_i = 0
mx_cnt = 0
mn_i = 0
mn_cnt = 0
arr = list(map(int, input().split()))
for i in range(n):
    if arr[i] > arr[mx_i]:
        mx_i = i
        mx_cnt = 1
    elif arr[i] == arr[mx_i]:
        mx_cnt += 1
    if arr[i] < arr[mn_i]:
        mn_i = i
        mn_cnt = 1
    elif arr[i] == arr[mn_i]:
        mn_cnt += 1
print(max(0, n - mx_cnt - mn_cnt))

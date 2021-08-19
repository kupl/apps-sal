from operator import itemgetter
n, q = list(map(int, input().split()))
cnt = 0
ans = [0] * (n)
arr = [0] * q
for i in range(q):
    arr[i] = list(map(int, input().split()))
    for j in range(arr[i][0] - 1, arr[i][1], 1):
        ans[j] += 1
        if ans[j] == 1:
            cnt += 1
cnt1 = [0] * (n + 1)
cnt2 = [0] * (n + 1)
# print("ans",*ans)
for i in range(n):
    cnt1[i + 1] = cnt1[i]
    cnt2[i + 1] = cnt2[i]
    if ans[i] == 1:
        cnt1[i + 1] += 1
    if ans[i] == 2:
        cnt2[i + 1] += 1
# print(cnt2)
mac = 0
for i in range(q):
    for j in range(i + 1, q, 1):
        delete = cnt1[arr[i][1]] - cnt1[arr[i][0] - 1] + cnt1[arr[j][1]] - cnt1[arr[j][0] - 1]
        if arr[j][0] > arr[i][1] or arr[j][1] < arr[i][0]:
            pass
        elif arr[j][0] <= arr[i][1]:
            # print("****",cnt2[min(arr[i][1],arr[j][1])],cnt2[max(arr[j][0]-1,arr[i][0]-1)])
            delete += cnt2[min(arr[i][1], arr[j][1])] - cnt2[max(arr[j][0] - 1, arr[i][0] - 1)]

        # print(i,j,delete)
        if cnt - delete > mac:
            mac = cnt - delete
print(mac)

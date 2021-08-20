N = int(input())
arr = []
temp = N
for i in range(2, int(N ** 0.5 // 1 + 1)):
    if temp % i == 0:
        cnt = 0
        while temp % i == 0:
            cnt += 1
            temp = temp // i
        arr.append(cnt)
if temp != 1:
    arr.append(1)
if arr == [] and N != 1:
    arr.append(1)
ans = 0
for i in range(len(arr)):
    for n in range(1, 100):
        if arr[i] >= n:
            ans += 1
            arr[i] -= n
        else:
            break
print(ans)

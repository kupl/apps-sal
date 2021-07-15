n = int(input())
arr = list(map(int, input().split()))
i = 0
last = 0
now = 0
ln = -1
flag = 0
for i in range(len(arr)):
    if arr[i] == arr[last]:
       now += 1
    else:
        if not (ln == -1 or ln == now):
            flag = 1
            break
        elif ln == -1:
            ln = now
            last = i
            now = 1
        else:
            last = i
            now = 1


if not flag and (ln == -1 or ln == now):
    print("YES")
else:
    print("NO")

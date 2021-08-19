n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
pos = [0] * (n + 1)
arr = [0] * (n + 1)
for i in range(len(a)):
    pos[a[i]] = i + 1
    arr[i + 1] = a[i]
l = 0
#print(pos, arr)
for i in b:
    if pos[i] % k:
        l += pos[i] // k + 1
    else:
        l += pos[i] // k
    if pos[i] - 1:
        tempPos = pos[i]
        tempArr = arr[pos[i] - 1]
        pos[i] -= 1
        pos[tempArr] += 1
        arr[pos[i]] = i
        arr[pos[i] + 1] = tempArr
print(l)

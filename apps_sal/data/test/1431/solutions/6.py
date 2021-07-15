n = int(input())
arr = list(map(int, input().split()))
count = 0
arr3 = [0]*n
arr5 = []
if list(set(arr)) == [0]:
    print(0)
    return
for j in range(n, 0, -1):
    cancer = 0
    pre = 0
    for k in range(j, n+1, j):
        pre += arr3[k - 1]
    if pre % 2 != arr[j-1]:
        count += 1
        arr5.append(j)
        arr3[j-1] += 1
print(count)
for aa in arr5:
    print(aa)

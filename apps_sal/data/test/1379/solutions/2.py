(n, m, d) = list(map(int, input().split()))
arr = list(map(int, input().split()))
arrx = []
for i in range(n):
    arrx.append((arr[i], i))
arrx.sort()
arr1 = [0] * n
arr1[arrx[0][1]] = 1
count = 1
index = 0
for i in range(1, n):
    if arrx[i][0] >= arrx[index][0] + d + 1:
        arr1[arrx[i][1]] = arr1[arrx[index][1]]
        index += 1
    else:
        count += 1
        arr1[arrx[i][1]] = count
print(count)
print(*arr1)

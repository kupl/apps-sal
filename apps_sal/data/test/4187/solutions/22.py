n = int(input())
arr = [int(x) for x in input().split()]
arr = arr + arr
m, cur = 0, 0
for i in range(len(arr)):
    if arr[i] == 1:
        m += 1
        cur = max(m, cur)
    else:
        m = 0
print(cur)

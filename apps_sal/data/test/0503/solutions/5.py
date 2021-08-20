(n, k) = list(map(int, input().split(' ')))
a = input().split(' ')
arr = {}
zeroes = 0
lst = {}
ans = 0
for i in a:
    i = int(i)
    if i == 0:
        zeroes += 1
    else:
        if i in list(arr.keys()):
            arr[i][0] += 1
            if i % k == 0 and i // k in list(lst.keys()):
                arr[i][1] += arr[i // k][0]
        else:
            arr[i] = [1, 0]
            if i % k == 0 and i // k in list(lst.keys()):
                arr[i][1] = arr[i // k][0]
            lst[i] = True
        if i % k == 0 and i // k in list(lst.keys()):
            ans += arr[i // k][1]
if k == 1:
    ans = 0
    for i in lst:
        ans += arr[i][0] * (arr[i][0] - 1) * (arr[i][0] - 2) // 6
ans += zeroes * (zeroes - 1) * (zeroes - 2) // 6
print(ans)

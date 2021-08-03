import collections
arr = [0] * 200010
query = int(input())
total = 0
l = 0
r = 0
ans = []
for test in range(query):
    ty, idd = [(x) for x in input().split()]
    idd = int(idd)
    if ty == 'L':
        l += 1
        arr[idd] = (1, l - 1)
        total += 1
    elif ty == 'R':
        r += 1
        arr[idd] = (0, r - 1)
        total += 1
    else:
        left = 0
        right = 0
        x = arr[idd]
        if x[0] == 0:
            left = l + x[1]
            right = r - x[1] - 1
        else:
            left = l - x[1] - 1
            right = r + x[1]
        ans.append(min(left, right))
    # print(arr)
for i in range(len(ans)):
    print(ans[i])

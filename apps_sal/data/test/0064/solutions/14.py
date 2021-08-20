(n, k) = map(int, input().split())
d = dict()
arr = input()
for i in range(len(arr)):
    if arr[i] in d:
        d[arr[i]] += 1
        if d[arr[i]] > k:
            print('NO')
            break
    else:
        d[arr[i]] = 1
else:
    print('YES')

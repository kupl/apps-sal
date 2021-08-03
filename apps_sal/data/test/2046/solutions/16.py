n = int(input())
arr = [0] + list(map(int, input().split()))
came = [False] * (n + 2)
put = [False] * (n + 2)
put[n + 1], came[n + 1] = True, True
for i in range(1, n + 1):
    if put[arr[i] + 1] == True:
        put[arr[i]] = True
        print(arr[i], end=' ')
        k = arr[i] - 1
        while came[k]:
            put[k] = True
            print(k, end=' ')
            k -= 1
        print()
    else:
        came[arr[i]] = True
        print()

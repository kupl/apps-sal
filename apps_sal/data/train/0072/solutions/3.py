for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    if len(set(arr)) > k:
        print(-1)
    else:
        result = []
        temp = list(set(arr))
        for i in range(1, n + 1):
            if len(temp) == k:
                break
            if i not in temp:
                temp.append(i)

        for i in range(len(arr)):
            result.extend(temp)
        print(len(result))
        print(*result)

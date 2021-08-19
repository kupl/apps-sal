for testcase in range(int(input())):
    (n, x) = map(int, input().split())
    arr = list(map(int, input().split()))
    start = 0
    for i in arr:
        if not i % x:
            start += 1
        else:
            break
    end = 0
    for i in arr[::-1]:
        if not i % x:
            end += 1
        else:
            break
    if start == end == len(arr):
        print(-1)
        continue
    else:
        total = sum(arr)
        if not total % x:
            print(len(arr) - min(start, end) - 1)
        else:
            print(len(arr))

n = int(input())
arr = list(map(int, input().split()))

arr = [(i, num) for num, i in enumerate(arr)]
arr.sort(key=lambda x: (-x[0], x[1]))

m = int(input())
for q in range(m):
    k, pos = tuple(map(int, input().split()))

    now = []
    for i in arr:
        if len(now) == k:
            break
        now.append(i)

    now.sort(key=lambda x: x[1])
    print(now[pos - 1][0])

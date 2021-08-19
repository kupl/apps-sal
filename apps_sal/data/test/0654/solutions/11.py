from itertools import accumulate
N = int(input())

arr = [1]

res = 1

for i in range(2, N + 1):
    arr = list(accumulate(arr))
    arr = arr + [arr[-1]]
    d = i + 1

    # print(arr)

    s = 0

    for i in range(len(arr)):
        s += arr[i] * (d // 2)
        d -= 1

    res += s

    res = res % 1000000007
    # print(res)

print(res)

import os


def __starting_point():
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    increase = [-1] * n
    decrease = [-1] * n
    tmp = n - 1
    for i in range(n - 1, -1, -1):
        if i != n - 1:
            if arr[i] > arr[i + 1]:
                tmp = i
        increase[i] = tmp
    tmp = 0
    for i in range(n):
        if i != 0:
            if arr[i - 1] < arr[i]:
                tmp = i
        decrease[i] = tmp
    result = []
    for i in range(m):
        a, b = list(map(int, input().split()))
        a -= 1
        b -= 1
        result.append("Yes\n" if increase[a] >= decrease[b] else "No\n")

    print("".join(result))


__starting_point()

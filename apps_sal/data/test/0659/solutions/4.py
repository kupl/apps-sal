def solve(arr):
    if len(arr) <= 2 or len(set(arr)) == 1:
        return [-1]
    else:
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] != arr[j]:
                    (arr[i], arr[j]) = (arr[j], arr[i])
                    if arr != sorted(arr) and arr != list(reversed(sorted(arr))):
                        return [i + 1, j + 1]
                    else:
                        (arr[i], arr[j]) = (arr[j], arr[i])
    return [-1]


def __starting_point():
    n = int(input())
    arr = list(map(int, input().split()))
    print(*solve(arr))


__starting_point()

import sys
input = sys.stdin.readline


def compress(array):
    array2 = sorted(set(array))
    memo = {value: index for index, value in enumerate(array2)}
    for i in range(len(array)):
        array[i] = memo[array[i]] + 1
    return array


t = int(input())
base = 10 ** 6
for _ in range(t):
    n, b = list(map(str, input().split()))
    n = int(n)
    ans = [0] * n

    now = base
    ans[0] = base
    for i in range(n - 1):
        if b[i] == ">":
            now -= base
            ans[i + 1] = now
        else:
            now += 1
            ans[i + 1] = now
    print(*compress(ans))

    now = base
    ans[0] = base
    for i in range(n - 1):
        if b[i] == ">":
            now -= 1
            ans[i + 1] = now
        else:
            now += base
            ans[i + 1] = now
    print(*compress(ans))

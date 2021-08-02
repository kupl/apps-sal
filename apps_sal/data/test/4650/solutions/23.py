t = int(input())


def solve(arr, n):
    ones = 0
    twos = 0
    for item in arr:
        if item % 3 == 1:
            ones += 1
        elif item % 3 == 2:
            twos += 1
    zeros = n - ones - twos
    threes = abs(ones - twos) // 3
    return zeros + min(ones, twos) + threes


for _ in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(solve(arr, n))

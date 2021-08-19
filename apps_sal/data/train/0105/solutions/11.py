import sys


def input():
    return sys.stdin.readline()[:-1]


def getInt():
    return int(input())


def getIntIter():
    return list(map(int, input().split()))


def getIntList():
    return list(getIntIter())


def flush():
    sys.stdout.flush()


for _ in range(getInt()):
    (n, k) = getIntIter()
    nums = getIntList()
    m = min(nums)
    ans = 0
    for num in nums:
        ans += (k - num) // m
    ans -= (k - m) // m
    print(ans)

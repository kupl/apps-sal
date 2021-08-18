from collections import defaultdict
from collections import deque
from collections import Counter
import math


def readInt():
    return int(input())


def readInts():
    return list(map(int, input().split()))


def readChar():
    return input()


def readChars():
    return input().split()


n, k = readInts()
a = readInts()

a.sort(reverse=True)

if n == 1:
    print((math.ceil(a[0] / (k + 1))))
    return


def get(left, right):
    l = (right - left) // 2 + left
    ans = 0
    for i in a:
        ans += math.ceil(i / l) - 1
    #print(l, ans, left, right)
    return ans, l


def nibu(left, right):
    ans, l = get(left, right)

    if left < right:
        if ans <= k:
            return nibu(left, l)
        else:
            return nibu(l + 1, right)
    else:
        return right


print((nibu(1, a[0])))

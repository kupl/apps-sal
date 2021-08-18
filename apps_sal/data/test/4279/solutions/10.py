'''input
5
1
3
20
38
56
'''
from sys import stdin, stdout, setrecursionlimit
import math
from bisect import bisect_left


def find_index(num):
    n = math.ceil((-1 + math.sqrt(1 + 8 * num)) / 2)
    index = num - (n * (n - 1)) // 2
    return index


arr = [0, 1]
s = 0
for i in range(2, 10 ** 6):
    arr.append(arr[-1] + arr[-1] - arr[-2])

    arr[-1] += len(str(i))
    if arr[-1] > 10 ** 9:
        break

search = [0]
for i in range(1, len(arr) + 1):
    m = list(str(i))
    for c in m:
        search.append(c)

q = int(stdin.readline().strip())
for _ in range(q):
    num = int(stdin.readline().strip())
    index = bisect_left(arr, num)
    print(search[num - arr[index - 1]])

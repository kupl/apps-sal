from collections import defaultdict
import collections
import math
N = int(input())
List = list(map(int, input().split()))
dicList = collections.Counter(List)
total = 0
for key in dicList:
    if dicList[key] >= 2:
        total += dicList[key] * (dicList[key] - 1) // 2
for item in List:
    print(total - dicList[item] + 1)

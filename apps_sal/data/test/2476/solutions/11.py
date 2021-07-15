import collections
import numpy as np

# リストarrからx個の同じ長さの列を取り出す時の最大の長さ
# 発想: x個取り出す時、ある文字をx個より多く取り出して列に含むことはない
#       一方ある文字をその文字がある数よりも取り出して使うこともできない
#       つまり、min(arr.count(a), x)で、x個の同じ長さの列に使えるaの数がわかる
#       さらに、sum(min(arr.count(a),x))で、x個の同じ長さの列に使える文字の数がわかる
#       よって、sum(min(arr.count(a),x))//xで、x個の同じ長さの列の長さがわかる
#       発展的に、longest(arr,x)までの計算状況からlongest(arr,x+1)が計算できる
# def longest(arr, x):    # legacy
#     return sum(min(arr.count(a), x) for a in arr) // x


n = int(input())
a = list(map(int, input().split()))

counter = collections.Counter(a)        #O(n)
nums = list(counter.values())           #O(n)
num_counter = collections.Counter(nums) #O(n)
lastest_add = np.count_nonzero(nums)    #O(n)
building, longests = [0], [0]
for i in range(1, n+1):                 #O(n)
    appended = building[-1] + lastest_add   #O(1)
    building.append(appended)               #O(1)
    longests.append(appended // i)          #O(1)
    lastest_add -= num_counter[i]           #O(1)


lastest_longest = 0
k_most = []
for i, x in enumerate(reversed(longests)):
    while x > lastest_longest:
        lastest_longest += 1
        k_most.append(n-i)

k_most.extend([0]*(n-len(k_most)))      # zero padding

for longests_num in k_most:
    print(longests_num)

# print('----------------')
# for k in range(1, n+1):
#     maxindexes = list(i for i, x in enumerate(longests) if x >= k)
#     if maxindexes:
#         print(maxindexes[-1])
#     else:
#         print(0)


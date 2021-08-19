__author__ = 'zihaozhu'
from sys import stdin
import operator
N = int(stdin.readline())
data = list(map(int, stdin.readline().split()))
count = dict()
prefix = list()
prefix.append(data[0])
for i in range(1, len(data)):
    prefix.append(data[i - 1] + data[i])
    data[i] = data[i - 1] + data[i]
for i in prefix:
    if not i in count:
        count[i] = 1
    else:
        count[i] = count[i] + 1
sorted_count = sorted(count.items(), key=operator.itemgetter(1), reverse=True)
k = sorted_count[0][1]
print(N - k)

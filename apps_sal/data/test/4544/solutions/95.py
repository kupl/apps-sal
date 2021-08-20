import collections
n = int(input())
a = list(map(int, input().split()))
c = a + [i - 1 for i in a] + [i + 1 for i in a]
cntList = collections.Counter(c)
print(cntList.most_common()[0][1])

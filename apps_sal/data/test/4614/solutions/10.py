import collections
l=list(map(int,input().split()))
counted = collections.Counter(l)
print(counted.most_common()[1][0])

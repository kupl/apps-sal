import collections as c
input()
print(sum((j if i > j else j - i for (i, j) in c.Counter(map(int, input().split())).items())))

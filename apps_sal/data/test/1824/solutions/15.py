from collections import *
n = input()
l = [(), (), ()]
for i in range(3):
    l[i] = Counter(input().split())
for t in l[0] - l[1]:
    print(int(t))
for t in l[1] - l[2]:
    print(int(t))

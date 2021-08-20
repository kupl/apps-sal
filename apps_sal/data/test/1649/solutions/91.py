import itertools
flag = True
l = list(map(int, input().split()))
for i in itertools.combinations(l, 2):
    if sum(list(i)) * 2 == sum(l):
        print('Yes')
        flag = False
        break
for i in itertools.combinations(l, 1):
    if flag and sum(list(i)) * 2 == sum(l):
        print('Yes')
        flag = False
if flag:
    print('No')

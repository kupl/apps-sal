import itertools
l = list(map(int, input().split()))
flag = True
ans = sum(l)

for i in itertools.combinations(l, 2):
    if sum(list(i)) * 2 == ans:
        print('Yes')
        flag = False
        break

for j in itertools.combinations(l, 1):
    if flag and sum(list(j)) * 2 == ans:
        print('Yes')
        flag = False

if flag:
    print('No')

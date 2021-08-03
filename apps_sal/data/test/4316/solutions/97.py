S = list(input())
if len([x for x in set(S) if S.count(x) > 1]) == 2:
    print('Yes')
else:
    print('No')

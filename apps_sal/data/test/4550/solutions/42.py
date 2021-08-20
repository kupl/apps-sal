abc = list(map(int, input().split()))
abc_max = max(abc)
abc2 = abc
abc2.remove(abc_max)
if abc_max == sum(abc2):
    print('Yes')
else:
    print('No')

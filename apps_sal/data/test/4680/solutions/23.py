from collections import Counter
N = dict(Counter(map(int, input().split())))
print('YES') if N[5] == 2 and N[7] == 1 else print('NO')

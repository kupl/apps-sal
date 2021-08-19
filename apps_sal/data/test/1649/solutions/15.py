import itertools
l = list(map(int, input().split()))
ans = False
for L in range(1, len(l)):
    for subset in itertools.combinations(l, L):
        if sum(subset) * 2 == sum(l):
            ans = True
            print('Yes')
            break
    if ans:
        break
if not ans:
    print('No')

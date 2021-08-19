N = int(input())
L = list(map(int, input().split()))
L = sorted(L)
if sum(L) - L[-1] > L[-1]:
    print('Yes')
else:
    print('No')

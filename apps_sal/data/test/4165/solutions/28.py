N = int(input())
L = list(map(int, input().split()))
L_max = max(L)
if sum(L) - L_max > L_max:
    print('Yes')
else:
    print('No')

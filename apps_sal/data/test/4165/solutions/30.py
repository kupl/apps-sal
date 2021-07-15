N = int(input())
L = list(map(int, input().split()))
sortL = sorted(L)
print('Yes' if sortL[-1] < sum(sortL[:-1]) else 'No')

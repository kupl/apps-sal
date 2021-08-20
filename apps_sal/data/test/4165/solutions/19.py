N = int(input())
L = list(map(int, input().split()))
descending_L = sorted(L, reverse=True)
other_side = sum(descending_L[1:])
if descending_L[0] < other_side:
    print('Yes')
else:
    print('No')

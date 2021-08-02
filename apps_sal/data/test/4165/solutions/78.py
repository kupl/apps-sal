N = int(input())
l = list(map(int, input().split()))

max_l = max(l)
sum_l = sum(l) - max_l

if sum_l - max_l > 0:
    print('Yes')
else:
    print('No')

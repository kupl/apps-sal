(h, n) = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
sum_a = sum(a)
if sum_a >= h:
    print('Yes')
else:
    print('No')

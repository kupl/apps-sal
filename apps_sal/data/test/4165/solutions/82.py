n = int(input())
al = list(map(int, input().split()))
al_max = max(al)
al_sum = sum(al)
if al_sum - al_max * 2 > 0:
    print('Yes')
else:
    print('No')

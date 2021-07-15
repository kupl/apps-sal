H,M = map(int,input().split())
attack = list(map(int,input().split()))
if H - sum(attack) <=0:
    print('Yes')
else:
    print('No')

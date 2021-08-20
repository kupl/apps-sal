(N, M) = map(int, input().split())
attack = list(map(int, input().split()))
if sum(attack) >= N:
    print('Yes')
else:
    print('No')

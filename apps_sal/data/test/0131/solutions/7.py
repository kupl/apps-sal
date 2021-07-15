n = int(input())
sx = sum(map(int, input().split()))
sy = sum(map(int, input().split()))
if sx >= sy:
    print('Yes')
else:
    print('No')

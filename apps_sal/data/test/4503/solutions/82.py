H, N = map(int, input().split())
data = list(map(int, input().split()))

if H - sum(data) > 0:
    print('No')
else:
    print('Yes')

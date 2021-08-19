(H, N) = map(int, input().split())
data = list(map(int, input().split()))
if H <= sum(data):
    print('Yes')
else:
    print('No')

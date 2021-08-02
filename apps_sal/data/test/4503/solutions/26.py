h, n = map(int, input().split())
li = list(map(int, input().split()))
if h <= sum(li):
    print('Yes')
else:
    print('No')

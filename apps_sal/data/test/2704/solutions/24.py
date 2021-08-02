x, y = map(int, input().split())
l = list(map(int, input().split()))
k = min(l)
l = max(l)
for i in range(y):
    a = int(input())
    if a >= k and a <= l:
        print('Yes')
    else:
        print('No')

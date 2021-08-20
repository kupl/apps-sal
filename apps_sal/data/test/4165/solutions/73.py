n = int(input())
l = list(map(int, input().split()))
terms = max(l) < sum(l) - max(l)
if terms:
    print('Yes')
else:
    print('No')

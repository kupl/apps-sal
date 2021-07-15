n = int(input())
l = list(map(int, input().split()))
m = max(l)

l.pop(l.index(m))

if m < sum(l):
    print('Yes')
else:
    print('No')

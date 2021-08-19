a = list(map(int, input().split()))
b = a.pop(a.index(max(a)))
if b == sum(a):
    print('Yes')
else:
    print('No')

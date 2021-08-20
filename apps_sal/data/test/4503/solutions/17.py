(h, n) = map(int, input().split())
l = list(map(int, input().split()))
a = 0
for i in range(n):
    a += l[i]
if a >= h:
    print('Yes')
else:
    print('No')

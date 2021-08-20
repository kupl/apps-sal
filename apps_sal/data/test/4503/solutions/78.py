(h, n) = map(int, input().split())
l = list(map(int, input().split()))
s = 0
for i in range(n):
    s = s + l[i]
if s >= h:
    print('Yes')
else:
    print('No')

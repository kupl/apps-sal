n = int(input())
l = list(map(int, input().split()))
l.sort()
tmp = 0
for i in range(n - 1):
    tmp += l[i]
if l[-1] < tmp:
    print('Yes')
else:
    print('No')

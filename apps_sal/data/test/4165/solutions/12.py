n = int(input())
l = list(map(int, input().split()))
l.sort()
sum = 0
for i in range(n - 1):
    sum += l[i]
if l[-1] < sum:
    print('Yes')
else:
    print('No')

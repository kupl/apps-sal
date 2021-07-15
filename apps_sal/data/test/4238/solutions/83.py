N = list(input())
tot = 0
for i in N:
    tot += int(i)
if tot % 9 == 0:
    print('Yes')
else:
    print('No')

N = int(input())
a = [int(x) for x in input().split()]
cnt4 = 0
cnt2 = 0
for x in a:
    if x % 4 == 0:
        cnt4 += 1
        continue
    if x % 2 == 0:
        cnt2 += 1
cnt2 = cnt2//2*2
if N-cnt2 > 2*cnt4+1:
    print('No')
else:
    print('Yes')

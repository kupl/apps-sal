N = int(input())
a = list(map(int, input().split()))
count = 0
hcount = 0
for x in a:
    if x % 4 == 0:
        count += 1
    elif x % 2 == 0:
        hcount += 1

if (count + (hcount // 2)) >= (N // 2):
    print('Yes')
else:
    print('No')

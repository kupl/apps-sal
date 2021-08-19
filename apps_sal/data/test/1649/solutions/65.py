li = list(map(int, input().split()))
li.sort()
if li[0] + li[3] == li[1] + li[2] or li[0] + li[1] + li[2] == li[3]:
    print('Yes')
else:
    print('No')

candy = sorted([int(x) for x in input().split()])
if candy[0] + candy[1] == candy[2]:
    print('Yes')
else:
    print('No')

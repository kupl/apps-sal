S = sorted(input())
T = sorted(input(), reverse=True)
if S >= T:
    print('No')
else:
    print('Yes')

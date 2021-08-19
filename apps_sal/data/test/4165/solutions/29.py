N = input()
i = list(map(int, input().split()))
if max(i) < sum(i) - max(i):
    print('Yes')
else:
    print('No')

n = int(input())
ls = list(map(int, input().split()))
if ls[0] % 2 == 1 and ls[-1] % 2 == 1 and (len(ls) % 2 == 1):
    print('Yes')
else:
    print('No')

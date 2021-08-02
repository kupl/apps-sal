b, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
ans = 0
for x in a:
    ans = ans * b + x
    ans %= 2
if ans == 0:
    print('even')
else:
    print('odd')

n = eval(input())
a = list(map(int, input().split()))
l = 0
for i in a:
    if i % 2 == 0:
        l += 1
if l > n - l:
    print('READY FOR BATTLE')
else:
    print('NOT READY')

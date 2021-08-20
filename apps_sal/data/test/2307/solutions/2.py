odd = 0
even = 0
eval(input())
for i in map(int, input().split()):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
if even > odd:
    print('READY FOR BATTLE')
else:
    print('NOT READY')

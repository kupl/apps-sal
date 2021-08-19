n = int(input())
ev = 0
odd = 0
i = 0
arr = list(map(int, input().split()))
for each in arr:
    if each % 2 == 0:
        ev += 1
    else:
        odd += 1
if ev > odd:
    print('READY FOR BATTLE')
else:
    print('NOT READY')

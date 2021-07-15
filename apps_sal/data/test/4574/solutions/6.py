from collections import Counter
n=int(input())
a=list(map(int,input().split()))

c=Counter(a)
can_make=[i[0] for i in c.items() if i[1]>=2]
can_make_square=[i[0] for i in c.items() if i[1]>=4]
can_make+=can_make_square
can_make.sort()

if len(can_make)<2:
    print(0)
else:
    print(can_make[-1]*can_make[-2])

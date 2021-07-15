n=int(input()) 
c=list(map(int, input().split()))
a = 0
a2 = 0
a4 = 0

for i in c:
    if i%2 != 0:
        a += 1
    if i%2 == 0 and i%4 != 0:
        a2 += 1
    if i%4 == 0:
        a4 += 1
if a == 0 :
    print('Yes')
if a > 0 and a2 == 0:
    if a <= a4 +1 :
        print('Yes')
    else:
        print('No')
if a > 0 and a2 > 0:
    if a <= a4 :
        print('Yes')
    else:
        print('No')

N = int(input())
a = list(map(int, input().strip().split()))
even = 0
odd = 0
four = 0
for n in range(N):
    if a[n] % 4 == 0:
        four += 1
    elif a[n] % 2 == 0:
        even += 1
    else:
        odd += 1
if odd == 0:
    print('Yes')
elif even == 0:
    if four >= odd - 1:
        print('Yes')
    else:
        print('No')
elif four >= odd:
    print('Yes')
else:
    print('No')

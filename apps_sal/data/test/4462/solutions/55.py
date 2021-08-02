n = int(input())
A = list(map(int, input().split()))

multi_4 = 0
multi_2 = 0
odd = 0
for a in A:
    if a % 4 == 0:
        multi_4 += 1
    elif a % 2 == 0:
        multi_2 += 1
    else:
        odd += 1

if multi_2 > 0:
    if odd > multi_4:
        print('No')
    else:
        print('Yes')
else:
    if odd > multi_4 + 1:
        print('No')
    else:
        print('Yes')

N = int(input())
A = list(map(int, input().split()))
four = 0
odd = 0
for a in A:
    if a % 2 == 1:
        odd += 1
    if a % 4 == 0:
        four += 1
if N % 2 == 1:
    if odd - four <= 1:
        print('Yes')
    else:
        print('No')
elif odd - four <= 0:
    print('Yes')
else:
    print('No')

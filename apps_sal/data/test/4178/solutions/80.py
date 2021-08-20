N = int(input())
fN = list(map(int, input().split()))
plus = True
if N != 1:
    for i in range(1, len(fN))[::-1]:
        if fN[i] < fN[i - 1]:
            if fN[i] + 1 == fN[i - 1]:
                fN[i - 1] -= 1
            else:
                plus = False
if plus:
    print('Yes')
else:
    print('No')

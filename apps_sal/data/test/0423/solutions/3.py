import sys
input = sys.stdin.readline
(n, k) = map(int, input().split())
coeff = [str(input().strip()) for _ in range(n + 1)]
if coeff.count('?') == 0:
    total = 0
    for s in range(n + 1)[::-1]:
        total = total * k + int(coeff[s])
        if abs(total) > 1000000000000:
            break
    if total == 0:
        print('Yes')
    else:
        print('No')
elif k == 0:
    if coeff[0] == '?':
        if (n + 1 - coeff.count('?')) % 2 == 1:
            print('Yes')
        else:
            print('No')
    elif coeff[0] == '0':
        print('Yes')
    else:
        print('No')
elif (n + 1) % 2 == 0:
    print('Yes')
else:
    print('No')

S, P = list(map(int, input().split()))
ans = False
for n in range(1, int(P ** (0.5)) + 1):
    if P % n == 0:
        m = P // n
        if n + m == S:
            ans = True
if ans:
    print('Yes')
else:
    print('No')

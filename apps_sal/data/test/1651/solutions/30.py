s, p = map(int, input().split())
flg = False
for m in range(1, 10**6 + 1):
    n = s - m
    if n > 0 and m * n == p:
        print('Yes')
        flg = True
        break
if not flg:
    print('No')

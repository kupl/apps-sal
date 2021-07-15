N = int(input())
a = list(map(int, input().split()))
n = 1
C = 0
for ai in a:
    if ai != n:
        C += 1
    else:
        n += 1
if n == 1:
    print('-1')
else:
    print(C)

(n, a, b) = list(map(int, input().split()))
d = list(map(int, input().split()))
low = min(a, b)
ANS = 0
check = 1
for i in range(n):
    if d[i] == 2:
        if d[n - i - 1] == 0:
            ANS += a
        elif d[n - i - 1] == 1:
            ANS += b
        else:
            ANS += low
for i in range(n):
    if d[i] == 0 and d[n - i - 1] == 1:
        check = 0
if check == 0:
    print(-1)
else:
    print(ANS)

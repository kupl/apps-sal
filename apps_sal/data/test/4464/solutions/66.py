def zz():
    return list(map(int, input().split()))


(a, b, c) = zz()
ans = 0
for i in range(1, b + 1):
    if a * i % b == c:
        ans = 1
        break
if ans == 0:
    print('NO')
else:
    print('YES')

k = int(input())
(a, b) = map(int, input().split())
cu = 0
for i in range(a, b + 1):
    if i % k == 0:
        cu += 1
        break
if cu >= 1:
    print('OK')
else:
    print('NG')

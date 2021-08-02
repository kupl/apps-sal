n = int(input())
a = list(map(int, input().split()))
s = 0
for i in a:
    s += i
if s - max(a) * 2 < 0:
    print('NO')
elif s % 2 == 0:
    print('YES')
else:
    print('NO')

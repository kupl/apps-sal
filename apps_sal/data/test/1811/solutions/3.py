n, k = map(int, input().split())
s = input()
long = 0
m = 0
for i in s:
    if i == '
    long += 1
    else:
        m = max(m, long)
        long = 0

if k > m:
    print('YES')
else:
    print('NO')

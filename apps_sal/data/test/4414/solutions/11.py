t = int(input())
for tt in range(t):
    (a, b, n, s) = map(int, input().split())
    temp = s // n
    aa = min(temp, a)
    s -= n * aa
    if b >= s:
        print('YES')
    else:
        print('NO')

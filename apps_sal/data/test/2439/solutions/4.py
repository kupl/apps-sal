# map(int, input().split())
rw = int(input())
for wewq in range(rw):
    n = int(input())
    a = list(map(int, input().split()))
    if sum(a) == 0:
        print('NO')
        continue
    a.sort()
    print('YES')
    if sum(a) > 0:
        a.reverse()
    for i in a:
        print(i, end=' ')
    print('')

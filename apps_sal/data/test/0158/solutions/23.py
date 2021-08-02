n = int(input())
a = list(sorted(list(map(int, input().split())), reverse=True))

if min(a[:n]) > max(a[n:]):
    print('YES')
else:
    print('NO')

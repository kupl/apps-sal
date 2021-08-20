n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.remove(0)
b.remove(0)
i = a.index(b[0])
if a[i:] + a[:i] == b:
    print('YES')
else:
    print('NO')

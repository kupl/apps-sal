n = int(input())
ar = list(map(int, input().split()))
ar.sort()
a = ar[:n]
b = ar[n:]
if len(set(a) & set(b)) == 0:
    print('YES')
else:
    print('NO')

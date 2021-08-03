n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = max(b)
del b[b.index(max(b))]
if sum(a) <= x + max(b):
    print('YES')
else:
    print('NO')

n, t = map(int, input().split())
a, cur = [0] + [int(x) for x in input().split()], 1
while cur < t:
    cur += a[cur]
print('YES' if cur == t else 'NO')

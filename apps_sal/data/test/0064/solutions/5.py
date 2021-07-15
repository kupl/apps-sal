n, k = map(int, input().split())
s = input()
d = dict()
for i in s:
    d[i] = d.get(i, 0) + 1
    if d[i] > k:
        print('NO')
        return
print('YES')

q = int(input())
out = []
for i in range(q):
    x, y = map(int, input().split())
    if x - y == 1:
        out.append('NO')
    else:
        out.append('YES')
print('\n'.join(out))

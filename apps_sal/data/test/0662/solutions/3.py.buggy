#map(int, input().split())
n = int(input())
a = [1, 2]
d = [1, 2, 3]
for i in range(n):
    aa = int(input())
    if aa in a:
        ii = (a.index(aa) + 1) % 2
        for j in range(3):
            if d[j] not in a:
                a[ii] = d[j]
                break
    else:
        print('NO')
        return
print('YES')

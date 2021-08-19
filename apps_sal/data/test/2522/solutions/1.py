n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = 0
c = True
for i in range(n):
    if i > 0:
        if a[i] != a[i - 1]:
            s = 0
    if a[i] != b[i]:
        continue
    else:
        c = False
        while s != n:
            if a[i] != b[s] and a[s] != b[i]:
                (b[i], b[s]) = (b[s], b[i])
                c = True
                break
            s += 1
        if not c:
            break
if not c:
    print('No')
else:
    print('Yes')
    print(*b)

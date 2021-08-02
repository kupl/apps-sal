

a = list(map(int, input().split()))
a = sorted(a)

s = sum(a)

for i in range(1 << 4):
    s1 = 0

    for j in range(4):
        if(i & (1 << j)):
            s1 += a[j]

    if(s1 == (s - s1)):
        print('YES')
        return

print('NO')

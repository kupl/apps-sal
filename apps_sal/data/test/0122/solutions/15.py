n = int(input())
a = list(map(int, input().split()))
e = set([0])
p = 0
s = sum(a)
if s % 2:
    st = False
else:
    st = True
if st:
    st = False
    for j in range(2):
        for i in a:
            p += i
            e.add(i)
            if p - s // 2 in e:
                st = True
                break
        e = set([0])
        p = 0
        a.reverse()
print('YES' if st else 'NO')

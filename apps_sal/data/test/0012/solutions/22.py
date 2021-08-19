def mi():
    return list(map(int, input().split()))


'\n10\nGGGSGGGSGG\n'
n = int(input())
s = list(input())
for i in range(n):
    if s[i] == 'G':
        s[i] = 1
    else:
        s[i] = 0
a = []
i = 0
while i < n:
    if s[i] == 1:
        c = 0
        zc = 0
        pz = -1
        while i < n and zc <= 1:
            if s[i] == 1:
                c += 1
            else:
                zc += 1
                if zc == 1:
                    pz = i
            i += 1
        a.append(c)
        if pz != -1:
            i = pz
    else:
        i += 1
if len(a) > 1:
    ans = max(a) + 1
    if ans > s.count(1):
        print(s.count(1))
    else:
        print(max(a) + 1)
elif len(a) == 1:
    print(a[0])
else:
    print(0)

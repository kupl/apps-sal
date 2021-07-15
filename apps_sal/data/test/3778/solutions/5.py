n = int(input())
a = list(map(int, input().split()))
if a[-1] > 1:
    print(-1)
    return
s = set()
s2 = []
s3 = []
r = 1
for i in range(n):
    if a[i] == 1:
        if s2:
            x = s2.pop()
            s.add((x, i + 1))
        elif s3:
            x = s3.pop()
            s.add((x, i + 1))
            s.add((r, i + 1))
            r += 1
        else:
            s.add((r, i + 1))
            r += 1
    elif a[i] == 2:
        if s3:
            x = s3.pop()
            s.add((x, i + 1))
            s.add((r, i + 1))
            s2.append(r)
            r += 1
        else:
            s.add((r, i + 1))
            s2.append(r)
            r += 1
    elif a[i] == 3:
        if s3:
            x = s3.pop()
            s.add((x, i + 1))
            s.add((r, i + 1))
            s3.append(r)
        else:
            s.add((r, i + 1))
            s3.append(r)
        r += 1
    else:
        r += 1
if s2 or s3:
    print(-1)
else:
    print(len(s))
    for x in s:
        print(x[0], x[1])


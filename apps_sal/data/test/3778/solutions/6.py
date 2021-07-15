n = int(input())
aa = list(map(int, input().split()))
r = 1
pen2 = []
pen3 = []
ans = []
for c, a in enumerate(aa, 1):
    if a == 0:
        pass
    elif a == 1:
        if pen2:
            b = pen2.pop()
            ans.append((b, c))
        elif pen3:
            b = pen3.pop()
            ans.append((b, c))
            ans.append((r, c))
            r += 1
        else:
            ans.append((r, c))
            r += 1
    elif a == 2:
        pen2.append(r)
        if pen3:
            b = pen3.pop()
            ans.append((b, c))
            ans.append((r, c))
            r += 1
        else:
            ans.append((r, c))
            r += 1
    else:
        if pen3:
            b = pen3.pop()
            ans.append((b, c))
            ans.append((r, c))
            pen3.append(r)
            r += 1
        else:
            ans.append((r, c))
            pen3.append(r)
            r += 1

if r > (n + 1) or pen2 or pen3:
    print(-1)
else:
    print(len(ans))
    print('\n'.join(' '.join(map(str, x)) for x in ans))


def ints():
    return list(map(int, input().split()))


def rd():
    return input()


n = ints()[0]
A = []
for i in range(n):
    (l, r) = ints()
    A.append((r, r - l))
A.sort()
(cnt, ct) = (0, 0)
for p in A:
    if ct + p[1] > p[0]:
        continue
    else:
        ct = p[0] + 1
        cnt += 1
print(cnt)

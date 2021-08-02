
def mi():
    return map(int, input().split())


n = int(input())
a = list(mi())

i1 = 0
i2 = n - 1

cand = []

s1 = s2 = 0
s1 += a[i1]
s2 += a[i2]
while i1 < i2:
    if s1 == s2:
        cand.append(s1)
        i1 += 1
        i2 -= 1
        if i1 == n or i2 == -1:
            break
        s1 += a[i1]
        s2 += a[i2]
    elif s1 < s2:
        i1 += 1
        if i1 == n or i2 == -1:
            break
        s1 += a[i1]
    else:
        i2 -= 1
        if i1 == n or i2 == -1:
            break
        s2 += a[i2]
if len(cand):
    print(cand[-1])
else:
    print(0)

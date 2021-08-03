n = int(input())
a = list(map(int, input().split()))

s1 = sum(a[1::2])
s2 = sum(a[2::2])

#print(s1, s2)


r = 0
if s1 == s2:
    r += 1

for i, aa in enumerate(a[1:], 1):
    if i % 2 == 1:
        s1 -= a[i]
        s1 += a[i - 1]
    else:
        s2 -= a[i]
        s2 += a[i - 1]

    if s1 == s2:
        r += 1

print(r)

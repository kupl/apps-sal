(A, B, C) = map(int, input().split())
l = sorted([A, B, C])
d = l[2] - l[0]
e = l[1] - l[0]
if d * e == 0:
    ans = d
elif d == e:
    ans = d // 2 + 2 * (d % 2)
elif d % 2 == e % 2 == 0:
    ans = d // 2 + (d - e) // 2
elif e % 2 == 0:
    ans = d // 2 + (d - e) // 2 + 1
elif d % 2 == 0:
    ans = d // 2 + (d - e) // 2 + 2
else:
    ans = d // 2 + (d - e) // 2 + 2
print(ans)

l = sorted(list(map(int, input().split())))
d, e, f = l[2] - l[0], l[1] - l[0], l[2] - l[1]
if d * e == 0:
    ans = d
elif f == 0:
    ans = d // 2 + 2 * (d % 2)
elif e % 2 == 0:
    ans = d // 2 + f // 2 + d % 2
else:
    ans = d // 2 + f // 2 + 2
print(ans)

a = [int(i) for i in input()]
if sum(a[3:]) > sum(a[:3]):
    (a[:3], a[3:]) = (a[3:], a[:3])
a[:3] = sorted(a[:3], reverse=True)
a[3:] = sorted(a[3:], reverse=True)
ans = 0
i = 0
j = 5
while sum(a[:3]) > sum(a[3:]):
    ans += 1
    if a[i] > 9 - a[j]:
        a[i] = 0
        i += 1
    else:
        a[j] = 9
        j -= 1
print(ans)

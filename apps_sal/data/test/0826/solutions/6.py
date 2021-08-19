n = int(input())


def func(ii):
    return (ii + 1) * ii // 2 - (n + 1)


l = 1
r = n
m = (r + l) // 2
while r - l > 1:
    m = (r + l) // 2
    if func(m) == 0:
        break
    if func(m) > 0:
        r = m
    if func(m) < 0:
        l = m
if func(r) == 0:
    c = r
elif func(m) <= 0:
    c = m
else:
    c = l
print(n - c + 1)

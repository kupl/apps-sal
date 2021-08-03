n = int(input())
t = len(str(n))
if t == 1:
    x = 0
else:
    x = int((t - 1) * '9')
y = n - x


def sm(x):
    res = 0
    for i in str(x):
        res += int(i)
    return res


print(sm(x) + sm(y))

n = int(input())
a = []


def rec(x):
    nonlocal n, a
    for i in [3, 5, 7]:
        if x * 10 + i > n:
            continue
        s = str(x * 10 + i)
        if "3" in s and "5" in s and "7" in s:
            a.append(x * 10 + i)
        rec(x * 10 + i)


for i in [3, 5, 7]:
    rec(i)
print((len(a)))


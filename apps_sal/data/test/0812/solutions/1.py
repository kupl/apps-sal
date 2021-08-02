n = int(input())
b = list(map(int, input().split()))
b_ = []
for i, t in enumerate(b):
    b_.append([t, i + 1])
b_.sort()


def solve(s):
    def check(a):
        if len(a) <= 1:
            return True
        delta = a[1] - a[0]
        for i in range(1, len(a) - 1):
            if a[i + 1] - a[i] != delta:
                return False
        return True

    if check([x[0] for x in s[1:]]):
        # print('a')
        return s[0][1]
    if check([x[0] for x in s[:-1]]):
        # print('b')
        return s[-1][1]
    if check([x[0] for x in s[:1] + s[2:]]):
        # print('c')
        return s[1][1]
    if check([x[0] for x in s[:-2] + s[-1:]]):
        # print('d')
        return s[-2][1]

    # mid
    t = []
    for i in range(len(s) - 1):
        t.append(s[i + 1][0] - s[i][0])
    # print(t)

    i = 0
    while t[i] == t[0]:
        i += 1
    j = len(t) - 1
    while t[j] == t[-1]:
        j -= 1

    if t[0] == t[-1]:
        if i != j - 1:
            return -1
        if t[i] + t[j] != t[0]:
            return -1
        return s[j][1]
    else:
        if i != j:
            return -1
        if i == 1 and t[0] + t[1] == t[2]:
            return s[1][1]
        if j == len(t) - 2 and t[j] + t[j + 1] == t[j - 1]:
            return s[len(t) - 1][1]
        return -1


print(solve(b_))

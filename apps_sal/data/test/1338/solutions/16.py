#file = open("", 'r')
#f = lambda:file.readline()
def f(): return input()


n, m = list(map(int, f().split()))

most = 0

p = []

for i in range(1, n + 1):
    p.append(i)
    most += i * (n + 1 - i)


def next_perm():
    i = len(p) - 1
    while i > 0 and p[i - 1] >= p[i]:
        i -= 1

    if i <= 0:
        return False

    j = len(p) - 1

    while p[j] <= p[i - 1]:
        j -= 1

    p[i - 1], p[j] = p[j], p[i - 1]

    j = len(p) - 1
    while(i < j):
        p[i], p[j] = p[j], p[i]
        i += 1
        j -= 1

    return True


def fp():
    s = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            s += min(p[i - 1:j])
    return s


while(m > 0):
    if (fp() == most):
        m -= 1
        if m == 0:
            break

    next_perm()

print(" ".join(str(e) for e in p))

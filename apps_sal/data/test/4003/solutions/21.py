n = int(input())
a = [int(i) for i in input().split()]
new = [0]
s = ''
i = 0
j = -1


def rec(a, i, j):
    c = func(a, i + 1, j, new + [a[i]], s)
    d = func(a, i, j - 1, new + [a[j]], s)
    if c[0] < d[0]:
        return True
    else:
        return False


def func(a, i, j, new, s):
    while True:
        if n - i < -j:
            return len(new) - 1, s
            break
        if a[i] > new[-1] and a[j] > new[-1]:
            if a[i] == a[j]:
                if rec(a, i, j):
                    new.append(a[j])
                    j -= 1
                    s += 'R'
                else:
                    s += 'L'
                    new.append(a[i])
                    i += 1
            elif a[i] < a[j]:
                new.append(a[i])
                s += 'L'
                i += 1
            else:
                new.append(a[j])
                s += 'R'
                j -= 1
        elif a[i] > new[-1] or a[j] > new[-1]:
            if a[i] > new[-1]:
                new.append(a[i])
                s += 'L'
                i += 1
            else:
                new.append(a[j])
                s += 'R'
                j -= 1
        else:
            return len(new) - 1, s
            break


for j in func(a, i, j, new, s):
    print(j)

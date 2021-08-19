(n, t) = (int(input()), sorted(map(int, input().split())))
(a, b, k) = ([t[0]], [], False)
for i in range(1, n):
    if t[i] == t[i - 1]:
        k = True
    else:
        if k:
            k = False
            b.append(t[i - 1])
        a.append(t[i])
print(len(a) + len(b))
print(' '.join(map(str, a)) + ' ' + ' '.join(map(str, reversed(b))))

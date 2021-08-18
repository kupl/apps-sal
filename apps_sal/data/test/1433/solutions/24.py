def f(s):

    l, r = s.find('1'), s.rfind('1')

    if l == -1:

        return 0

    else:

        return l + len(s) - r - 1 + 2 * sum(s[i] == '0' for i in range(l + 1, r))


n, m = list(map(int, input().split()))

a = [''.join(input().split()) for i in range(n)]

r = sum(f(s) for s in a)

c = sum(f(''.join(a[i][j] for i in range(n))) for j in range(m))

print(r + c)

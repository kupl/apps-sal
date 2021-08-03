n, m, l = list(map(int, input().split()))
a = list(map(int, input().split()))
c = 0
if a[0] > l:
    c += 1
    a[0] = 0
for i in range(1, n):
    if a[i] > l:
        a[i] = 0
        if a[i - 1] != 0:
            c += 1
for i in range(m):
    s = input()
    if s[0] == '0':
        print(c)
    else:
        _, x, y = list(map(int, s.split()))
        if a[x - 1] <= l and a[x - 1] != 0:
            if a[x - 1] + y > l:
                if x != 1 and x != n and a[x - 2] != 0 and a[x] != 0:
                    c += 1
                    a[x - 1] = 0
                elif x == 1 and n != 1 and a[x] != 0:
                    a[x - 1] = 0
                    c += 1
                elif x == n and n != 1 and a[x - 2] != 0:
                    a[x - 1] = 0
                    c += 1
                elif x != 1 and x != n and a[x - 2] == 0 and a[x] == 0:
                    c -= 1
                    a[x - 1] = 0
                elif n == 1:
                    if c == 0:
                        c = 1
                else:
                    a[x - 1] = 0
            else:
                a[x - 1] += y

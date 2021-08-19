def R(): return list(map(int, input().split()))


n, m, s, f = R()


if s < f:

    d = 1

    c = 'R'

else:

    d = -1

    c = 'L'


res = ""

i = 1

j = s

t, l, r = R()

k = 1

while j != f:

    if i > t and k < m:

        t, l, r = R()

        k += 1

    if i == t and (l <= j <= r or l <= j + d <= r):

        res += 'X'

    else:

        res += c

        j += d

    i += 1


print(res)


# Made By Mostafa_Khaled

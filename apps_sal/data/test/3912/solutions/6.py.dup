from collections import Counter

n = int(input())
inp = input()

c = Counter(inp)

t = len(list([x for x in list(c.values()) if x % 2 == 1]))

if t == 0:
    temp = sum([[list(c.items())[j][0]] * (list(c.items())[j][1] // 2) for j in range(len(list(c.items())))], [])

    print(1)
    print(''.join(temp) + ''.join(temp[::-1]))

else:
    ones = list()
    for j in range(len(list(c.items()))):
        i = list(c.items())[j]
        if i[1] % 2 == 1:
            c[list(c.keys())[j]] -= 1
            ones.append(i[0])

    others = sum([[list(c.items())[j][0]] * (list(c.items())[j][1] // 2) for j in range(len(list(c.items())))], [])

    while n % t != 0 or n // t % 2 == 0:
        t += 2
        o = others.pop()
        ones.append(o)
        ones.append(o)
    L = n // t

    ans = list()
    ot = 0
    for i in range(t):
        mid = str()
        if L % 2 == 1:
            mid = ones[i]
        ln = L // 2
        ans.append(''.join(others[ot: ot + ln]) + mid + ''.join(others[ot: ot + ln][::-1]))
        ot += ln

    print(t)
    print(' '.join(ans))

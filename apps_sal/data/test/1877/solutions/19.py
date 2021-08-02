n = int(input())
S = input()

c = ([0, 1], [1, 0])[S[0] == 'R']
f = c[0] == 1

ans = 0
for el in S[1:]:
    if el == 'R':
        c[0] += 1

        if not f and c[0] - c[1] == 1:
            ans += 1
            f = not f

    elif el == 'U':
        c[1] += 1

        if f and c[1] - c[0] == 1:
            ans += 1
            f = not f

    else:
        exit(100500)

print(ans)

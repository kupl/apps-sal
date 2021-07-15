n, k, l = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

d = [abs(x - y) for x, y in zip(a, b)]

moves = k + l

d.sort()
d.reverse()

while moves > 0:
    if d[0] == 0:
        print(moves%2)
        break

    d[0] -= 1

    c = 0

    while c < n - 1 and d[c] < d[c + 1]:
        d[c], d[c + 1] = d[c + 1], d[c]
        c += 1

    moves -= 1
else:
    print(sum([x**2 for x in d]))

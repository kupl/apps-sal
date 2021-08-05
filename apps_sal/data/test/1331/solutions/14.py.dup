n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))

a = list(sorted(a))
s = []
r = 0

for x in a:
    if len(s) and s[0] < x - m + 1:
        del s[0]

    if len(s) < k - 1:
        s.append(x)

    else:
        r += 1

print(r)

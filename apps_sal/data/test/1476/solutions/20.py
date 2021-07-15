n = int(input())
if n == 1:

    res = [1]

else:

    even, odd = list(range(2, n + 1, 2)), list(range(1, n + 1, 2))
    l, r = sorted((even, odd), key=lambda c: c[-1], reverse=True)
    while r and abs(l[-1] - r[0]) == 1:

        r.pop(0)

    res = l + r

print(len(res))
print(str.join(" ", list(map(str, res))))


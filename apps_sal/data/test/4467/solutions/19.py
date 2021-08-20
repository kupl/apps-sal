(n, *ABCD) = map(int, open(0).read().split())
AB = sorted([(a, b) for (a, b) in zip(ABCD[:2 * n:2], ABCD[1:2 * n:2])], key=lambda x: -x[1])
CD = sorted([(c, d) for (c, d) in zip(ABCD[2 * n::2], ABCD[2 * n + 1::2])])
for (c, d) in CD:
    for i in range(len(AB)):
        (a, b) = AB[i]
        if a < c and b < d:
            _ = AB.pop(i)
            break
print(n - len(AB))

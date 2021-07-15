import string

for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    s = input()
    p = list(map(int, input().split())) + [-1]

    d = {c: [0] for c in string.ascii_lowercase}

    for i in s:
        for c in string.ascii_lowercase:
            d[c].append(d[c][-1])

        d[i][-1] += 1

    ans = {c: 0 for c in string.ascii_lowercase}

    for i in p:
        for c in string.ascii_lowercase:
            ans[c] += d[c][i]

    print(*list(ans.values()))


def process(str):
    d = {}
    for c in str:
        d[c] = d.setdefault(c, 0) + 1
    return d


def match(d1, d2, case):
    ans = 0
    for c in d1:
        if case(c) not in d2:
            continue
        m = min(d1[c], d2[case(c)])
        ans += m
        d1[c] -= m
        d2[case(c)] -= m
    return ans


sd = process(input())
td = process(input())
yay = match(sd, td, lambda x: x)
whoops = match(sd, td, lambda x: x.lower() if x.isupper() else x.upper())
print(yay, whoops)

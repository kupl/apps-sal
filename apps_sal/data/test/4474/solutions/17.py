def to_string(n):
    res = ''
    while(n):
        res = str(n % 3) + res
        n //= 3
    res = list(res)
    return res


def to_int(s):
    res = 0
    for i in range(len(s)):
        res *= 3
        res += int(s[i])
    return res


q = int(input())
for _ in range(q):
    n = int(input())
    s = to_string(n)
    good = False
    while(not good):
        cnt = 0
        idx = 10000
        for i in range(len(s)):
            if (s[i] == '2'):
                cnt += 1
                idx = min(idx, i)
        if (cnt == 0):
            good = True
        if (not good):
            for i in range(idx + 1, len(s)):
                s[i] = '0'
            n = to_int(s)
            n += 3**(len(s) - idx - 1)
            s = to_string(n)
    print(n)

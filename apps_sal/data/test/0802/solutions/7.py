def pro():
    n = int(input())
    s = input()
    l = 0
    r = 0
    p = len(set(s))
    m = 100001
    y = len(s)
    k = set(s[0])
    d = dict()
    d[s[0]] = d.get(s[0], 0) + 1
    while r < y:
            if len(k)<p:
                r += 1
                if r < y:
                    k.add(s[r])
                    d[s[r]] = d.get(s[r], 0) + 1
            else:
                m = min(m, r - l + 1)
                if d[s[l]] == 1:
                    d[s[l]] = 0
                    k.remove(s[l])
                else:
                    d[s[l]] -= 1
                l += 1

    print(m)
pro()


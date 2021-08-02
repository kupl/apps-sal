n = int(input())
a = []
d = {}

for _ in range(n):
    s = input()
    g = set()
    for i in range(len(s)):
        for k in range(i, len(s)):
            st = s[i:k + 1]
            if st in g:
                continue
            else:
                g.add(st)
            if st in d:
                d[st] += 1
            else:
                d[st] = 1
    a.append(s)

for s in a:
    ans = s
    for i in range(len(s)):
        for j in range(i, len(s)):
            k = s[i:j + 1]
            if d[k] == 1 and len(k) < len(ans):
                ans = k
    print(ans)

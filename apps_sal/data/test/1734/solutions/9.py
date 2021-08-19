n = int(input())
m = {}
a = []
for i in range(n):
    s = input()
    sub = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            k = s[i:j + 1]
            if k in sub:
                continue
            else:
                sub.add(k)
            if k in m:
                m[k] += 1
            else:
                m[k] = 1
    a.append(s)
for s in a:
    ans = s
    for i in range(len(s)):
        for j in range(i, len(s)):
            k = s[i:j + 1]
            if m[k] == 1 and len(k) < len(ans):
                ans = k
    print(ans)

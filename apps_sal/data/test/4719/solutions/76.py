n = int(input())
s1 = input()
d = {}

for i in range(len(s1)):
    if s1[i] in d:
        d[s1[i]] += 1
    else:
        d[s1[i]] = 1

for i in range(n-1):
    di = {}
    s = input()
    for i in range(len(s)):
        if s[i] in di:
            di[s[i]] += 1
        else:
            di[s[i]] = 1

    delete = []
    for key, value in d.items():
        if key in di:
            d[key] = min(value, di[key])
        else:
            delete.append(key)

    for key in delete:
        del d[key]

ans = ""

for key, value in sorted(d.items()):
    ans += key*value

print(ans)

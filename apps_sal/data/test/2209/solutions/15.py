n = int(input())
a = []
for i in range(n):
    s = input()
    l = 0
    for c in s:
        if c == "s":
            l += 1
    a.append((s, l / len(s)))
a.sort(key=lambda x: x[1], reverse=True)
ns = 0
ans = 0
for st, _ in a:
    for c in st:
        if c == 's':
            ns += 1
        else:
            ans += ns
print(ans)

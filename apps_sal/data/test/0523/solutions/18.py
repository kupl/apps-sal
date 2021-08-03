n, m = list(map(int, input().split()))
strings = []
pal = []
pairs = []

for i in range(n):
    s = input()
    r = s[::-1]
    if s == r:
        pal.append(s)
    else:
        if r in strings:
            pairs.insert(0, s)
            pairs.append(r)
            strings.remove(r)
        else:
            strings.append(s)
l = len(pairs)
ans = ''
for i in range(l // 2):
    ans += pairs[i]
if pal:
    ans += max(pal, key=lambda a: len(a))
for i in range(l // 2):
    ans += pairs[l // 2 + i]
print(len(ans))
print(ans)

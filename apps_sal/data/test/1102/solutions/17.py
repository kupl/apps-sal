(n, a) = map(int, input().split())
a -= 1
criminal = list(map(int, input().split()))
l = []
r = []
r = criminal[a + 1:]
l = criminal[:a][::-1]
ans = 0
if criminal[a] == 1:
    ans += 1
s = min(len(r), len(l))
for i in range(s):
    if l[i] == r[i]:
        ans += 2 * l[i]
if len(r) > len(l):
    ans += sum(r[s:])
elif len(l) > len(r):
    ans += sum(l[s:])
print(ans)

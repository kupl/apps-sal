n = int(input())
a = list(map(int, input().split()))
s = set(a)
d = {}
for i in s:
    d[i] = 0
for i in a:
    d[i] += 1
ans = 0
for i in d:
    c = d[i]
    if c < i:
        ans += c
    elif c >= i:
        ans += c - i
print(ans)

MOD = 10**9 + 7
def I(): return list(map(int, input().split()))


s = input()
res = 0
n = len(s)
st = -1
e = -1
for i in range(n):
    if s[i] == '[':
        st = i
        break
for i in range(n - 1, -1, -1):
    if s[i] == ']':
        e = i
        break
# print(st , e)
if st > e or st == -1 or e == -1:
    print(-1)
    return
a = -1
b = -1
for i in range(st, e):
    if s[i] == ':':
        a = i
        break
for i in range(e, st, -1):
    if s[i] == ':':
        b = i
        break
if a == b or a == -1 or b == -1:
    print(-1)
    return
count = 0
for i in range(a, b):
    if s[i] == '|':
        count += 1
print(4 + count)

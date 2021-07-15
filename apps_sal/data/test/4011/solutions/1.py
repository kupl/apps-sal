n = int(input())
s = input()
d = input().split()
x = 0
for i in s:
    if d[int(i) - 1] > i:
        break
    x += 1
r = s[:x]
p = x
for i in s[x:]:
    if d[int(i) - 1] >= i:
        r += d[int(i) - 1]
    else:
        r += s[p:]
        break
    p += 1
print(r)

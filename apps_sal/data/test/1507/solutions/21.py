(n, k) = (int(i) for i in input().split())
s = input()
a = [0] * n
b = []
x = k
y = 0
alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
end = [s.rfind(i) for i in alf]
begin = [s.find(i) for i in alf]
f = False
ans = False
for i in range(n):
    find = alf.find(s[i])
    if i != end[find] and (not s[i] in b) or begin[find] == end[find]:
        b.append(s[i])
        x -= 1
    elif i == end[find] and i != begin[find]:
        x += 1
    if x < 0:
        ans = True
        break
    if begin[find] == end[find]:
        x += 1
print('YES' if ans else 'NO')

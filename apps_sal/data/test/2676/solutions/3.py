n = int(input())
l = []
for u in range(n):
    s = input()
    l.append(s)
m = int(input())
x = input()
ans = 0
t = []
for i in range(m):
    for j in range(i, m):
        t.append(x[i:j + 1])
t = list(set(t))
for i in t:
    if i in l:
        ans += 1
print(ans)

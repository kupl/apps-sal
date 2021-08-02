
n, s, t = map(int, input().split())
l = []
mp = map(int, input().split())
for i in mp:
    l.append(i)
a = [-1 for i in range(n)]
cur = 0
next = s
for i in range(n):
    cur = next
    if a[cur - 1] == -1:
        a[cur - 1] = i
    else:
        break
    next = l[cur - 1]
    # print(a)

print(a[t - 1])

h, w = map(int, input().split())
a = []
for i in range(h):
    b = [int(i) % 2 for i in input().split()]
    a.append(b)
c = []
odd = 0
n = 0
while n < h:
    if odd == 0:
        for i in range(w):
            c.append([n, i])
        odd = 1
    elif odd == 1:
        for i in range(w - 1, -1, -1):
            c.append([n, i])
        odd = 0
    n += 1
ans = []
for i in range(len(c)):
    if a[c[i][0]][c[i][1]] == 1:
        if i == len(c) - 1:
            break
        ans.append([str(c[i][0] + 1), str(c[i][1] + 1), str(c[i + 1][0] + 1), str(c[i + 1][1] + 1)])
        a[c[i + 1][0]][c[i + 1][1]] += 1
print(len(ans))
for i in range(len(ans)):
    print(' '.join(ans[i]))

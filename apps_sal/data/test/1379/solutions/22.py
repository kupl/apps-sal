(n, m, d) = list(map(int, input().split()))
a = list(map(int, input().split()))
l = []
for i in range(n):
    l.append((a[i], i))
l.sort()
j = 0
ans = [0] * n
c = 0
for i in range(n):
    if l[i][0] - d <= l[j][0]:
        c += 1
        ans[l[i][1]] = c
    else:
        ans[l[i][1]] = ans[l[j][1]]
        j += 1
print(c)
print(*ans)

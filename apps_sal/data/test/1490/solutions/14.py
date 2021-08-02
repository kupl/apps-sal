n, m = (int(x) for x in input().split())
a = [int(x) for x in input().split()]
a.sort()
i = 0
c = 1
ans = []
n_ans = 0
while ((m > 0) and (i < n)):
    if (c != a[i]):
        m -= c
        if (m >= 0):
            ans.append(c)
            n_ans = n_ans + 1
    if (c == a[i]):
        i = i + 1
    c = c + 1


while (m > 0):
    m -= c
    if (m >= 0):
        ans.append(c)
        n_ans = n_ans + 1
    c = c + 1

print(n_ans)
for i in range(n_ans):
    print(ans[i], ' ', sep='', end='')

from bisect import insort
n = int(input())
a = list(map(int, input().split()))
cm = [0] * (n + 1)
for i in range(n):
    cm[i + 1] = cm[i] + a[i]
d = dict()
for i in range(n):
    for j in range(i, n):
        sm = cm[j + 1] - cm[i]
        if sm in d:
            insort(d[sm], (j, i))
        else:
            d[sm] = [(j, i)]
ans = 0
arr = list()
tmparr = [None] * n
for sm in d:
    ct = 0
    end = -1
    for el in d[sm]:
        if el[1] > end:
            # print(ct,el)
            tmparr[ct] = el
            ct += 1
            end = el[0]
    if ct > ans:
        # print(sm)
        ans = ct
        # print(tmparr[:ans])
        arr = tmparr[:ans]
# print(d)
print(ans)
for el in arr:
    print(el[1] + 1, el[0] + 1)

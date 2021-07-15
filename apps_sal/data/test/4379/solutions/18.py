input()
a = list(map(int, input().split()))

b = {i: 0 for i in set(a)}

ans = 0
ans_ind = 0
for i in range(len(a)):
    if a[i] - 1 in b.keys():
        b[a[i]] = b[a[i] - 1] + 1
    else:
        b[a[i]] = 1
    if (b[a[i]] > ans):
        ans = b[a[i]]
        ans_ind = i
print(ans)
s = ""
aans = []
aans.append(ans_ind + 1)
x = a[ans_ind]
for i in range(ans - 1):
    while (a[ans_ind] != x - 1):
        ans_ind -= 1
    x = a[ans_ind]
    aans.append(ans_ind + 1)
for i in aans[::-1]:
    print(i, end=' ')

h, w = map(int, input().split())
A = []
ans = []
for i in range(h):
    A.append(list(input()))
for a in A:
    if a != ['.'] * w:
        ans.append(a)
counter = []
for i in range(w):
    flag = 0
    for j in range(len(ans)):
        if ans[j][i] == '
        flag = 1
        break
    if flag == 1:
        counter.append(i)

for a in ans:
    tmp = ''
    for i in counter:
        tmp = tmp + a[i]
    print(tmp)

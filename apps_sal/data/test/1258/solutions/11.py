n = int(input())
ar = []
for i in range(n - 2):
    ar.append(list(map(int, input().split())))

br = [False] * n
vr = [0] * n
rel = dict()
ans = []

for i in range(n):
    rel[i + 1] = set()

for i in range(n - 2):
    a = ar[i][0]
    b = ar[i][1]
    c = ar[i][2]

    rel[a].add(b)
    rel[a].add(c)
    rel[b].add(a)
    rel[b].add(c)
    rel[c].add(a)
    rel[c].add(b)


for i in range(n):
    if len(rel[i + 1]) == 2:
        start = i + 1
        break


br[start - 1] = True
ans.append(start)
for i in rel[start]:
    if len(rel[i]) == 3:
        ans.append(i)
        br[i - 1] = True
    else:
        x = i
ans.append(x)
br[x - 1] = True

i = 1
while(i < n - 2):
    for j in rel[ans[i]]:
        if br[j - 1] == False:
            ans.append(j)
            br[j - 1] = True
            break
    i += 1

for i in range(n):
    print(ans[i], end=" ")
print()

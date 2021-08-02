n = int(input())
l = list(map(int, input().split(" ")))
r = list(map(int, input().split(" ")))

slr = [l[i] + r[i] for i in range(n)]
ans = [n - slr[i] for i in range(n)]

flag = True
if l[0] != 0 or r[n - 1] != 0:
    flag = False

for i in range(n):
    great = 0
    for j in range(i + 1, n):
        if ans[i] < ans[j]:
            great = great + 1
    if r[i] != great:
        flag = False
        break
for i in range(n - 1, -1, -1):
    great = 0
    for j in range(i - 1, -1, -1):
        if ans[i] < ans[j]:
            great = great + 1
    if l[i] != great:
        flag = False
        break

if flag:
    print("YES")
    for i in range(0, n - 1):
        print(ans[i], end=" ")
    print(ans[n - 1])
else:
    print("NO")

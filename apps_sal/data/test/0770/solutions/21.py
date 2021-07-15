m = int(input())
l = list(map(int, input().split()))
p = 0
f = False
for i in range(m):
    if l[i] == 1 and f == False:
        p = p + 1
        if i + 1 < m:
            if l[i + 1] == 0:
                f = True
    if l[i] == 0 and f == True:
        p = p + 1
        f = False
if l[m - 1] == 0 and p > 0:
    p = p - 1
print(p)


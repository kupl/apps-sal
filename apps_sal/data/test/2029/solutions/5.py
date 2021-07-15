# list(map(int, input().split()))
n, s = list(map(int, input().split()))
ss = [[] for i in range(n)]
vis = [0] * n
#print(vis)
for i in range(n - 1):
    a, b = list(map(int, input().split()))
    ss[a - 1].append(b - 1)
    ss[b - 1].append(a - 1)

li = 0
#print(ss)


for i in range(n):
    if len(ss[i]) == 1:
        li += 1
print(s / li * 2)


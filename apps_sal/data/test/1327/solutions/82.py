n,m = map(int,input().split())
l = [list(map(int,input().split())) for _ in range(n)]
l0 = []
for i in range(8):
    lst = []
    for j in range(3):
        lst.append(i >> j & 1)
    l0.append(lst)

def f(x,i):
    return x*((-1)**i)
ans = 0
for i in range(8):
    lst = []
    for j in range(n):
        lst.append(
            f(l[j][0],l0[i][0])
            +f(l[j][1],l0[i][1])
            +f(l[j][2],l0[i][2])
        )
    lst.sort(reverse=True)
    ans = max(ans, sum(lst[:m]))
print(ans)

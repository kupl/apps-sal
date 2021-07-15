N = int(input())
dlst = list(map(int, input().split()))
ans = 0
for i in range(len(dlst)-1):
    k = dlst.pop()
    ans = ans + k*sum(dlst)

print(ans)

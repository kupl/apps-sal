n = int(input())
ans = {}
for i in range(n):
    a, x = list(map(int, input().split()))
    ans[a] = x
m = int(input())
for i in range(m):
    a, x = list(map(int, input().split()))
    if a in ans:
        if ans[a] < x:
            ans[a] = x
    else:
        ans[a] = x
s = 0
for i in ans:
    s += ans[i]
print(s)

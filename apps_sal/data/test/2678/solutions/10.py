n = int(input())
x = [list(map(int,input().split())) for i in range(n)]
x.sort(key = lambda i: i[1])
ans = 1
t = x[0]
for i in range(1,n):
    if x[i][0] > t[1]:
        ans += 1
        t = x[i]
print(ans)

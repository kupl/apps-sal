n = int(input())
lst = [list(map(int,input().split())) for i in range(n)]
lst.sort(key = lambda i: i[1])
res = 1
t = lst[0]
for i in range(1,n):
    if lst[i][0] > t[1]:
        res += 1
        t = lst[i]
print(res)

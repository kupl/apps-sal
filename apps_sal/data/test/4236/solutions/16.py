n, m = map(int, input().split())
s = []
k = 0
ans = []
for i in range(n):
    l, r= map(int,input().split())
    s.append((l ,r))
for i in range(1, m + 1):
    flag = True
    for j in range(n):
        if s[j][0] <= i <= s[j][1]:
            flag = False
    if flag:
        k = k + 1
        ans.append(i)
print(k, end=' \n')
for i in range(k):
    print(ans[i], end=' ')

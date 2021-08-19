n = int(input())
mas = list(map(int, input().split()))
ans = []
for i in range(n):
    ans.append([mas[i] - i, mas[i]])
ans.sort()
maxi = 0
p = -100000000
s = 0
for i in range(n):
    if ans[i][0] == p:
        s += ans[i][1]
    else:
        p = ans[i][0]
        maxi = max(maxi, s)
        s = ans[i][1]
maxi = max(maxi, s)
print(maxi)
#print (*ans)

n = int(input())
L, R = 0, 0
a = []
for i in range(n):
    l, r = map(int, input().split())
    L += l
    R += r
    a.append([l, r])
ans = [L, R, 0]
for i in range(n):
    nL = L - a[i][0] + a[i][1]
    nR = R - a[i][1] + a[i][0]
    #print(abs(ans[0] - ans[1]), abs(nL - nR))
    if abs(ans[0] - ans[1]) < abs(nL - nR):
        ans = [nL, nR, i + 1]
print(ans[2]) 

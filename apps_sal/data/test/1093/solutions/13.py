n, m = map(int, input().split())
u, d = 0, 0
ans1 = 0
ans2= 0
data = [input() for i in range(n)]
for i in range(m):
    help = ''
    for j in range(n):
        help += data[j][i]
    u = d
    d = n - help.find('*')
    delt = d - u
    if i != 0:
        if delt < 0:
            ans2 = max(ans2, abs(delt))
        else:
            ans1 = max(ans1, abs(delt))
print(ans1, ans2)

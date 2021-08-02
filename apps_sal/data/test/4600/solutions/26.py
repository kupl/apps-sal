n, m = map(int, input().split())
q = [0 for i in range(n)]
a = [False for i in range(n)]
ans1 = 0
ans2 = 0
for i in range(m):
    p, S = input().split()
    p = int(p) - 1
    if S == 'AC':
        a[p] = True
    else:
        if a[p] == False:
            q[p] += 1
for i in range(n):
    if a[i] == True:
        ans1 += 1
        ans2 += q[i]
print(ans1, ans2)

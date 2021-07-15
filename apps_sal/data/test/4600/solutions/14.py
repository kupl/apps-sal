N,M = map(int, input().split())
ans = [0]*N
ac = 0
p = 0

for m in range(M):
    a,b = map(str, input().split())
    a = int(a) - 1

    if ans[a] != -1 and b == 'WA':
        ans[a] += 1
    if ans[a] != -1 and b == 'AC':
        ac += 1
        p += ans[a]
        ans[a] = -1

print(ac,p)

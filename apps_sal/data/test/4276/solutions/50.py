(N, T) = list(map(int, input().split()))
ct = []
for i in range(N):
    tmp = list(map(int, input().split()))
    ct.append(tmp)
ct.sort()
ans = 0
for i in range(len(ct)):
    if ct[i][1] <= T:
        ans = ct[i][0]
        break
if ans == 0:
    print('TLE')
else:
    print(ans)

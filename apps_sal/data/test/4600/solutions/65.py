N, M = map(int, input().split())
ACs = [0] * (N+1)
Ps = [0] * (N+1)
for _ in range(M):
    p, s = input().split()
    p = int(p)
    if s == 'AC':
        ACs[p] = 1
    elif s == 'WA': # WA
        if ACs[p] == 0: 
            Ps[p] += 1

ans1 = sum(ACs)
ans2 = 0
for i in range(1, N+1):
    if ACs[i] == 1:
        ans2 += Ps[i]
print(ans1, ans2)

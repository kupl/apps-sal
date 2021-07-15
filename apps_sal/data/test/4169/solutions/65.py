N, M = map(int, input().split())
AB = []
for _ in range(N):
    AB.append(list(map(int, input().split())))

AB = sorted(AB)
cnt = 0
ans = 0
for ab in AB:
    if cnt+ab[1] <= M:
        cnt += ab[1]
        ans += ab[0]*ab[1]
    else:
        ans += (M-cnt)*ab[0]
        cnt += M-cnt
        break
    
print(ans)

N = int(input())
P = []
for i in range(N):
    s = input()
    s = sorted(s)
    P.append(s)
P = sorted(P)
last = P[0]
cnt = 0
ans = 0
for i in range(1, N):
    if P[i] == last:
        cnt += 1
        ans += cnt
    else:
        last = P[i]
        cnt = 0
print(ans)

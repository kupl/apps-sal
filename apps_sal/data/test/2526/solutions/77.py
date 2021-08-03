X, Y, A, B, C = list(map(int, input().split()))
P = sorted(list(map(int, input().split())), reverse=True)
Q = sorted(list(map(int, input().split())), reverse=True)
R = sorted(list(map(int, input().split())), reverse=True)

pq = sorted(P[:X] + Q[:Y])
cnt = 0
for i in range(min(C, X + Y)):
    if R[i] <= pq[i]:
        break
    cnt += 1

ans = sum(pq[cnt:]) + sum(R[:cnt])

print(ans)

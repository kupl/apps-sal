N,M = map(int,input().split())

H = list(map(int,input().split()))

ans = 0

H2 = []
for i in range(N):
    H2.append([0])

for i in range(M):
    A,B = map(int,input().split())
    
    H2[A-1].append(H[B-1])
    H2[B-1].append(H[A-1])

for i in range(N):
    H2[i] = max(H2[i])

for i in range(N):
    if H2[i] < H[i]:
        ans += 1

print(ans)

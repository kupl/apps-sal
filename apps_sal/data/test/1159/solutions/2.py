M = 10**5 + 2
prime = [0] * M
for i in range(2, M):
    if prime[i]:
        continue
    for j in range(i, M, i):
        if not prime[j]:
            prime[j] = i

N = int(input())

Edge = [(i, i + 1) for i in range(1, N)] + [(1, N)]

D = N
Nh = N // 2
cnt = 1
while prime[D] != D:
    D += 1
    Edge.append((cnt, cnt + Nh))
    cnt += 1
print(len(Edge))
for e in Edge:
    print(*e)

N, M = map(int, input().split())
AB = []

for _ in range(N):
    A, B = map(int, input().split())
    AB.append((A, B))

AB.sort()

i = 0
ans = 0

while M > 0:
    A, B = AB[i]
    if B <= M:
        ans += A * B
        M -= B
    else:
        ans += A * M
        M = 0
    i += 1

print(ans)

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB = sorted(AB, key=lambda x: x[0])

ans = 0
count = 0
for i in range(N):
    a, b = AB[i]

    if M - count <= b:
        c = M - count
        count += c
        ans += a * c
        break

    count += b
    ans += a * b

print(ans)

N = int(input())

answer = N * (N + 1) * (N + 2) // 6
for _ in range(N - 1):
    u, v = map(int, input().split())
    if u > v:
        u, v = v, u
    answer -= u * (N - v + 1)

print(answer)

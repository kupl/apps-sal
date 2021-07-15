n = int(input())

s = list(map(int, list(input())))

lights = []

for _ in range(n):
    a, b = list(map(int, input().split()))

    lights.append([a, b])

ans = sum(s)

for tick in range(1000):
    for i in range(n):
        if tick >= lights[i][1] and (tick - lights[i][1]) % lights[i][0] == 0:
            s[i] += 1
            s[i] %= 2
    ans = max(ans, sum(s))


print(ans)


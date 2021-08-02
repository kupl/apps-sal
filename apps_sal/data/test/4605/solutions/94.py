
N, A, B = map(int, input().split())

ans = 0

for i in range(N + 1):
    x = i % 10
    if i >= 10:
        x += (i % 100 - i % 10) / 10
        if i >= 100:
            x += (i % 1000 - i % 100) / 100
            if i >= 1000:
                x += (i % 10000 - i % 1000) / 1000
                if i == 10000:
                    x = 1
    if A <= x <= B:
        ans += i

print(ans)

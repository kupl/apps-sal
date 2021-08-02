A, B = map(int, input().split())

ans = 0

for i in range(1, 10):
    for j in range(10):
        for k in range(10):
            if A <= i * 10000 + j * 1000 + k * 100 + j * 10 + i <= B:
                ans += 1
print(ans)

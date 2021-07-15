k = 1
ans = 0
a, b = list(map(int, input().split()))
for i in range(60):
    k <<= 1
    d = 1
    for j in range(i):
        if a <= (k - (d << j) - 1) <= b:
            ans += 1
print(ans)


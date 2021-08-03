n, x = list(map(int, input().split()))
min_m = 1000
res = 0
for i in range(n):
    m = int(input())
    min_m = min(m, min_m)
    x -= m
    res += 1

res += x // min_m
print(res)

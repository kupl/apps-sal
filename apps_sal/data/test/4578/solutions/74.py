n, x = map(int, input().split())
min_m = 1000
count = 0
for _ in range(n):
    m = int(input())
    min_m = min(min_m, m)
    x -= m
    count += 1

count += x // min_m
print(count)

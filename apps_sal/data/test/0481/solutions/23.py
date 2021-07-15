n, q = list(map(int, input().split()))
count = 0
for var in range(1, n + 1):
    if (q / var) % 1 == 0 and q // var <= n:
        count += 1
print(count)


N = int(input())

ans = N * 2
i = 1
while i * i <= N:
    if N % i == 0:
        ans = min(ans, N // i + i)
    i += 1

print(ans - 2)

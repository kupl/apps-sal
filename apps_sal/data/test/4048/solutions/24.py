N = int(input())
cnt = 10**12
for i in range(1, int(N**.5) + 1):
    if N % i == 0:
        cnt = min(cnt, i + N // i - 2)
print(cnt)

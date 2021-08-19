N = int(input())
ans = 100000
for i in range(1, 13 * 10 ** 6):
    if N % i == 0:
        ans = min(ans, max(len(str(i)), len(str(N // i))))
print(ans)

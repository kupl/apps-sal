N = int(input())
ans = 100000
for i in range(1, 10 ** 5):
    if N % i == 0:
        ans = min(ans, max(len(str(i)), len(str(N // i))))
print(ans)

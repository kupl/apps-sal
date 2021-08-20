import bisect
N = int(input())
ans = 0
i = 2
a = [j * (j + 1) // 2 for j in range(64)]
while i * i <= N:
    cnt = 0
    while N % i == 0:
        N //= i
        cnt += 1
    ans += bisect.bisect_right(a, cnt) - 1
    i += 1
if N > 1:
    ans += 1
print(ans)

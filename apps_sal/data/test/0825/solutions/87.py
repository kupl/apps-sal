N = int(input())

ans = 0
for i in range(2, N):
    if i * i > N:
        break
    e = 0
    while N % i == 0:
        e += 1
        N //= i
    if e > 0:
        for j in range(1, 10):
            if e >= j:
                e -= j
                ans += 1
            else:
                break
if N > 1:
    ans += 1

print(ans)

N, M = list(map(int, input().split()))
ans = 1
for i in range(1, int(M**0.5)+1):
    if M % i == 0 and M//N >= i:
        ans = max(ans, i)
        if M//N >= M//i:
            ans = max(ans, M//i)
print(ans)


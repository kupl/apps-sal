N = int(input())
ans = 0
for i in range(1, N):
    if N % i != 0:
        ans += N // i
    else:
        ans += N // i - 1
print(ans)

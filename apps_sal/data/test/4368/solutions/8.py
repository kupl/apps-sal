(n, k) = map(int, input().split())
ans = 1
while True:
    n = n // k
    if n == 0:
        break
    ans += 1
print(ans)

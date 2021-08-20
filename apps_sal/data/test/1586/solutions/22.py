N = int(input())
if N % 2 == 0:
    ans = 0
    x = 10
    while x <= N:
        ans += N // x
        x *= 5
else:
    ans = 0
print(ans)

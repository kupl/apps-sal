n, k = list(map(int, input().split()))
cnt = 0
if k == 1:
    print(n)
    return
while(n):
    n //= 2
    cnt += 1
ans = 0
while(cnt):
    ans += 2 ** (cnt - 1)
    cnt -= 1
print(ans)


K = int(input())
if K % 2 == 0 or K % 5 == 0:
    print(-1)
    return
r = 7 % K
ans = 1
while r != 0:
    r = (r * 10 + 7) % K
    ans += 1
print(ans)

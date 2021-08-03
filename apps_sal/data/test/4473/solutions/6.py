t = int(input())
for cas in range(t):
    a, b, k = map(int, input().split())
    ans = (a - b) * (k // 2)
    if(k % 2 == 1):
        ans += a
    print(ans)

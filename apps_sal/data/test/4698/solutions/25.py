n = int(input())
t = list(map(int, input().split()))
m = int(input())
for j in range(m):
    ans = 0
    p, x = map(int, input().split())
    for k in range(n):
        if p == k + 1:
            ans += x
        else:
            ans += t[k]
    print(ans)

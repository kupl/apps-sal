n = int(input())
x = list(map(int, input().split()))

ans = 10**18
for i in range(1, 101):
    t = 0
    for j in range(n):
        t += (x[j] - i)**2
    ans = min(ans, t)
print(ans)

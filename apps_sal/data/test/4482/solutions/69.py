n = int(input())
a = list(map(int, input().split()))

ans = 10**9
for i in range(-100, 101):
    cost = 0
    for j in a:
        cost += (j-i)**2
    ans = min(ans, cost)
print(ans)

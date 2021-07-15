N = int(input())
X = list(map(int, input().split()))

ans = 10**9

for i in range(1, 101):
    total = 0
    for x in X:
        total += (x - i)**2
    ans = min(ans, total)
print(ans)

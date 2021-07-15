n = int(input())
k = int(input())
points = list(map(int, input().split()))

ans = 0
for i in points:
    minimum = min(abs(k-i), abs(i))
    ans += minimum*2

print(ans)

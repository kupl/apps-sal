n = int(input())
l = list(map(int, input().split()))
ans = float('inf')
for v in range(min(l), max(l) + 1):
    c = sum([(a - v)**2 for a in l])
    ans = min(ans, c)
print(ans)

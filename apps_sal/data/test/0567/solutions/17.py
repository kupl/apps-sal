n = int(input())
a = list(map(int, input().split()))
middle = 500000
ans = -1
for pr in a:
    ans = max(ans, min(pr - 1, 1000000 - pr))
print(ans)

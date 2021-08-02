n = int(input())
p = list(map(int, input().split()))

ans = 0
for val in p:
    ans = max(ans, min(abs(1 - val), abs(10**6 - val)))
print(ans)

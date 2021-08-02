n = int(input())
ans = prev = 0
for h in map(int, input().split()):
    if prev <= h:
        ans += 1
        prev = h
print(ans)

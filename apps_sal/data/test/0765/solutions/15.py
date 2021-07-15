T, S, q = map(int, input().split())
ans = 0
while S < T:
    S *= q
    ans += 1
print(ans)

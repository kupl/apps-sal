(n, m) = map(int, input().split())
ar = list(map(int, input().split()))
br = list(map(int, input().split()))
ans = []
for x in ar:
    if x in br:
        ans.append(x)
print(*ans)

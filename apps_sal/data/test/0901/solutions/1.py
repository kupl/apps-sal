n, m = map(int, input().split())
ans = "NO"
for i in range(m):
    v = set(list(map(int, input().split()))[1:])
    ans = "YES"
    for vi in v:
        if -vi in v:
            ans = "NO"
            break
    if ans == "YES":
        break
print(ans)

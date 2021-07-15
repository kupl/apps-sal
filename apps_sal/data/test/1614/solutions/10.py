n, h = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in a:
    ans += (i + h - 1) // h
print(ans)

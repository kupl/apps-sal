n = int(input())
ans = "YES"
a = int(1e9)
for _ in range(n):
    h, w = list(map(int, input().split()))
    if max(h, w) <= a:
        a = max(h, w)
    elif min(h, w) <= a:
        a = min(h, w)
    else:
        ans = "NO"
print(ans)


n = int(input())

a, b = map(int, input().split())
ans = min(a, b) + 1
for i in range(n - 1):
    c, d = map(int, input().split())
    if c > a or d > b:
        e = max(a, b)
        f = min(c, d)
        ans += max(0, f - e + 1)
        if a == b:
            ans -= 1
        #print(ans)
    a, b = c, d
    
print(ans)

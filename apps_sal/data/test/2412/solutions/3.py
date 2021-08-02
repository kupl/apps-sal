t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    f = 0
    while f < n and s[f] != '8':
        f += 1
    if f == n or n - f < 11:
        print("NO")
    else:
        print("YES")

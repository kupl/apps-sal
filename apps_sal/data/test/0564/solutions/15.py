n, s = map(int, input().split())
t = list(map(int, input().split()))
t = sorted(t)
if sum(t[:n - 1]) <= s:
    print("YES")
else:
    print("NO")

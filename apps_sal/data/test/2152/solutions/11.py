n = int(input())
(a, p) = list(map(int, input().split()))
minpref = p
ans = a * p
for i in range(n - 1):
    (a, p) = list(map(int, input().split()))
    minpref = min(minpref, p)
    ans += a * minpref
print(ans)

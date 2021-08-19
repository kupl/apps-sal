n = int(input())
L = list(map(int, input().split()))
e = 0
p = 0
ans = 0
for i in range(n):
    diff = p - L[i]
    e += diff
    if e <= 0:
        ans += -e
        e = 0
    p = L[i]
print(ans)

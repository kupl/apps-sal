n = int(input())
P = list(map(int, input().split()))
ans = 0
for i in range(n - 2):
    a = P[i]
    b = P[i + 1]
    c = P[i + 2]
    if a < b and b < c or (c < b and b < a):
        ans += 1
print(ans)

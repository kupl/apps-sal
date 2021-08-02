n = int(input())
k = int(input())
L = list(map(int, input().split()))
ans = 0
for l in L:
    a = l
    b = abs(k - l)
    ans += min(a, b) * 2
print(ans)

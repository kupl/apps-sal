(n, k) = map(int, input().split())
ans = 1
n1 = n
while n1 // k >= 1:
    n1 = n1 // k
    ans += 1
print(ans)

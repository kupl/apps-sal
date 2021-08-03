a, b = list(map(int, input().split()))
ans = 0
k = 1
while k < b:
    k -= 1
    k += a
    ans += 1
print(ans)

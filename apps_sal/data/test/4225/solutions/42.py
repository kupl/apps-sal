(a, b, c, k) = list(map(int, input().split()))
ans = 0
if a >= k:
    ans = k
elif a + b >= k:
    ans = a
else:
    ans = a + (k - a - b) * -1
print(ans)

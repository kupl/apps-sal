w, a, b = list(map(int, input().split()))

if a <= b:
    ans = max(0, b - (a + w))
else:
    ans = max(0, a - (b + w))
print(ans)

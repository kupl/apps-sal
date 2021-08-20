(l, r, x, y, k) = list(map(int, input().split()))
ans = 'NO'
for b in range(x, y + 1):
    a = k * b
    if l <= a <= r:
        ans = 'YES'
        break
print(ans)

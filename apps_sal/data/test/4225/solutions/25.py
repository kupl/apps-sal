[A, B, C, K] = list(map(int, list(input().split(' '))))
left = K
ans = 0
left = K - A
if left >= 0:
    ans += A
else:
    ans += K
left = left - B
if left > 0:
    ans -= left
print(ans)

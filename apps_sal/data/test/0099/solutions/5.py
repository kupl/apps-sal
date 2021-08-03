b, q, l, m = list(map(int, input().split()))
A = set(map(int, input().split()))

ans = 0
for _ in range(100):
    if abs(b) > l:
        break
    if b not in A:
        ans += 1
    b *= q
if ans > 40:
    print("inf")
else:
    print(ans)

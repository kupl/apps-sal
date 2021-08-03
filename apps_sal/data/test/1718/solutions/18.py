N, K = map(int, input().split())
A = list(map(int, input().split()))

ind1 = 0
for i, a in enumerate(A):
    if a == 1:
        ind1 = i
        break
left = ind1
right = N - ind1 - 1
ans = 0

a, b = divmod(left, K - 1)
a += 1 if b > 0 else 0
ans += a
if b > 0:
    right -= (K - 1 - b)
a, b = divmod(right, K - 1)
a += 1 if b > 0 else 0
ans += a

print(ans)

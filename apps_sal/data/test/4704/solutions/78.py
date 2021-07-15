with open(0) as f:
    N, *a = map(int, f.read().split())
score = -sum(a[1:]) + a[0]
ans = abs(score)
for x in a[1:N-1]:
    score += 2*x
    ans = min(ans, abs(score))
print(ans)

T = input().strip()
n = len(T)
p = n // 2
g = n - p
A = 'g' * g + 'p' * p
ans = 0
for (a, t) in zip(A, T):
    if a == 'p' and t == 'g':
        ans += 1
    if a == 'g' and t == 'p':
        ans -= 1
print(ans)

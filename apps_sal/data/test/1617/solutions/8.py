n = int(input())
ans = []
for d in range(1, n):
    if n < d * d:
         break
    if n % d != 0:
         continue
    ans.append(n * (d - 1) // 2 + d)
    if d * d < n:
        ans.append(n * (n // d - 1) // 2 + n // d)	
ans = list(sorted(ans))
print(' '.join(map(str, ans)))


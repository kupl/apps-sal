n, k = map(int, input().split())
rem = n % (2 * k + 1)

if n <= k + 1:
    ans = [1]
elif rem <= k and rem != 0:
    ans = range(k + 1 - (k + 1 - rem), n + 1, 2 * k + 1)
else:
    ans = range(k + 1, n + 1, 2 * k + 1)

print(len(ans))
print(' '.join(str(k) for k in ans))

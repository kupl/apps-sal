n, k = [int(v) for v in input().split()]
if 2 * k + 1 >= n:
    ans = [n // 2]
else:
    rem = n % (2 * k + 1)
    if rem == 0:
        ans = list(range(k, n, 2 * k + 1))
    else:
        ans = list(range(rem // 2, n, 2 * k + 1))

print(len(ans))
print(' '.join(str(v + 1) for v in ans))


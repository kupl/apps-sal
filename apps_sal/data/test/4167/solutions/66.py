(n, k) = map(int, input().split())
rem0 = n // k
remhalf = n // k + 1 if n // k * k + k // 2 <= n else n // k
ans = rem0 ** 3 + (remhalf ** 3 if k % 2 == 0 else 0)
print(ans)

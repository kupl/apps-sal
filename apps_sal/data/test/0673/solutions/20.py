def cin(): return map(int, input().split())


n, k = cin()
print((n // k) * k + k)

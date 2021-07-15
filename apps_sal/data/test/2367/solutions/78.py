mod = 10**9 + 7
h, w, a, b = map(int, input().split())

fact = [1] * (h + w + 1)
invf = [1] * (h + w + 1)
invn = [1] * (h + w + 1)
for i in range(2, h + w + 1):
  fact[i] = fact[i-1] * i % mod
  invn[i] = (-invn[mod % i]) * (mod // i) % mod
  invf[i] = invf[i-1] * invn[i] % mod

count = 0
for i in range(min(h-a, w-b)):
  count += fact[h+b-a-1] * invf[h-a-i-1] * invf[b+i] * fact[w+a-b-1] * invf[a+i] * invf[w-b-i-1]
  count %= mod
print(count)

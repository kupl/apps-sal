import string
(n, k) = (int(i) for i in input().split())
str = string.ascii_lowercase[:k]
ans = str * (n // k) + str[:n % k]
print(ans)

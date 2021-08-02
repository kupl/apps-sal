n, k = map(int, input().split())
nk = n % k
print(min(nk, abs(nk - k)))

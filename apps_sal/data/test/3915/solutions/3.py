p, q = (int(x) for x in input().split())
top = 1200000
isPrime = [1] * top
isPrime[1] = 0
palindromic = 1
res = 1
for i in range(2, top):
    if str(i) == str(i)[::-1]:
        palindromic += 1
    if isPrime[i]:
        for j in range(i * i, top, i):
            isPrime[j] = 0
    isPrime[i] += isPrime[i - 1]
    if q * isPrime[i] <= p * palindromic:
        res = i
print(res)

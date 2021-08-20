(n, k) = map(int, input().split(' '))
s = list(map(int, input().split(' ')))
result = s[-1]
while k * 2 > n:
    n -= 1
    k -= 1
if n > 0:
    for i in range(int(n / 2)):
        result = max(result, s[i] + s[n - 1 - i])
print(result)

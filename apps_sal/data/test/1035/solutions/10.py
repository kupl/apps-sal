def division(n):
    if n < 2:
        return [1]
    prime_factors = [1]
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            prime_factors.append(i)
            n //= i
    if n > 1:
        prime_factors.append(n)
    return prime_factors


(a, b) = map(int, input().split())
da = set(division(a))
db = set(division(b))
cnt = 0
for i in da:
    if i in db:
        cnt += 1
print(cnt)

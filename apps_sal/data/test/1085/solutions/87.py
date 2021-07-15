def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors
                
n = int(input())

a = make_divisors(n)
b = make_divisors(n - 1)

d = list(set(a + b))

ans = 0

for i in list(d):
    if i == 1:
        continue
    x = n
    while x % i == 0:
        x /= i
    
    if x % i == 1:
        ans += 1

print(ans)

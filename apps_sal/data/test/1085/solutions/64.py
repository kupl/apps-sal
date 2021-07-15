n = int(input())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    return divisors

a = make_divisors(n)
b = make_divisors(n-1)

ans = (len(b) - 1)
for i in a:
    x = n
    if i == 1:
        continue
    elif i == n:
        ans += 1
    else:
        while x % i == 0:
            x /= i
        if x % i == 1:
            ans += 1

print(ans)


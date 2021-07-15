import sys
def divisors(n,TF):
    divisors = []
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if TF == 1:
                if i != n // i:
                    divisors.append(n//i)
    return divisors
N = int(input())
if N == 2:
    print((1))
    return

ans = len(divisors(N - 1, 1)) + 2
A = divisors(N, 0)
for i in A:
    x = N
    while x % i == 0:
        x //= i
    if x % i == 1:
        ans += 1
print(ans)


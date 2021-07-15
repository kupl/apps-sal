# 約数
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

N = int(input())
divs = make_divisors(N)
# print(sorted(divs))
divs2 = make_divisors(N-1)
ans = len(sorted(divs2))-1
for div in divs[1:]:
    tmp = N
    while tmp%div == 0:
        tmp //= div
    if tmp%div == 1:
        ans += 1
print(ans)

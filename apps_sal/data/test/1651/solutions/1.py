import sys
s,p = map(int,input().split())
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors
ls = make_divisors(p)
for i in ls:
    if i + p//i == s:
        print("Yes")
        return
print("No")

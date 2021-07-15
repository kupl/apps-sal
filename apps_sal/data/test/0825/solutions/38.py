n = int(input())

if n == 1:
    print(0)
    return

def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0: return False
    return True

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            divisors.append(i)
            if i!=n//i:
                divisors.append(n//i)
    divisors.sort()
    return divisors
 
ans = []
cnt = 0
X = make_divisors(n)[1:]
for x in X:
    if is_prime(x):
        ans.append(x)
        n //= x
        cnt += 1
        e = 2
        while x**e < n:
            ans.append(x**e)
            e += 1
    elif x in ans:
        if n%x == 0:
            n //= x
            cnt += 1
print(cnt)

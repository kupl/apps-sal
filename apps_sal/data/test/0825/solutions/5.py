from collections import Counter

def prime_fact(num):
    prime = []
    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0:
            prime.append(i)
            num //= i
    if num != 1:
        prime.append(num)
    return prime

n = int(input())
cnt = Counter(prime_fact(n))

ans = 0
for c in cnt.values():
    tmp = 1
    while c >= tmp:
        c -= tmp
        ans += 1
        tmp += 1      
print(ans)

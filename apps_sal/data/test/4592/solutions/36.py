from collections import Counter

def factor(n):
    Ret = []
    for i in range(2, n + 1):
        while n % i == 0:
            n = n // i
            Ret.append(i)
    if len(Ret) == 0:
        return [n, ]
    else:
        return Ret

n = int(input())
fact = []

for i in range(2, n + 1):
    fact += factor(i)

ans = 1
for k, v in Counter(fact).items():
    ans *= v + 1
    ans %= 10**9 + 7
print(ans)

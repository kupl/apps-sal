from collections import Counter


def factor(n):
    res = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            res.append(i)
            n //= i
    if n > 1:
        return res + [n]
    else:
        return res


N = int(input())
ps = factor(N)
sq = [i * (i + 1) // 2 for i in range(100)]
ans = 0
for k, v in list(Counter(ps).items()):
    for i in range(99):
        if sq[i] <= v < sq[i + 1]:
            ans += i
            break
print(ans)

